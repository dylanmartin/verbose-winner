from nvflare.apis.impl.controller import Controller, Task
from nvflare.apis.fl_context import FLContext
from nvflare.apis.signal import Signal

class AverageWorkflow(Controller):
    def __init__(
        self,
        aggergator_id="aggregator",
        aggregator=None
    ):
        pass

    def start_controller(self, fl_ctx: FLContext) -> None:
        self.aggregator = self._engine.get_component(self.aggregator_id)
        pass

    def stop_controller(self, fl_ctx: FLContext):
        pass

    def control_flow(self, abort_signal: Signal, fl_ctx: FLContext) -> None:

        get_local_average_task = Task(
            name="get_local_average_and_count",
            data={},
            timeout=self._train_timeout,
            # before_task_sent_cb=self._prepare_train_task_data,
            result_received_cb=self._accept_site_result,
        )

        self.broadcast_and_wait(
            task=get_local_average_task,
            min_responses=self._min_clients,
            wait_time_after_min_received=self._wait_time_after_min_received,
            fl_ctx=fl_ctx,
            abort_signal=abort_signal,
        )

        aggr_result = self.aggregator.aggregate(fl_ctx)

    def _accept_site_result(self, client_name: str, result: Shareable, fl_ctx: FLContext) -> bool:
        accepted = self.aggregator.accept(result, fl_ctx)
        return accepted
