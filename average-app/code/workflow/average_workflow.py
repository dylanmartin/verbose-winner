from nvflare.apis.impl.controller import Controller, Task, ClientTask
from nvflare.apis.fl_context import FLContext
from nvflare.apis.signal import Signal
from nvflare.apis.shareable import Shareable
from nvflare.app_common.app_constant import AppConstants

class AverageWorkflow(Controller):
    def __init__(
        self,
        aggregator_id="aggregator",
        min_clients: int = 2,
        num_rounds: int = 2,
        start_round: int = 0,
        wait_time_after_min_received: int = 10,
        train_timeout: int = 0,
        ignore_result_error: bool = False,
        task_check_period: float = 0.5,
        persist_every_n_rounds: int = 1,
        snapshot_every_n_rounds: int = 1,
    ):
        super().__init__()
        self.aggregator_id = aggregator_id
        self.aggregator = None
        self._train_timeout = train_timeout
        self._min_clients = min_clients
        self._num_rounds = num_rounds
        self._start_round = start_round
        self._wait_time_after_min_received = wait_time_after_min_received
        self._ignore_result_error = ignore_result_error
        self._task_check_period = task_check_period
        self._persist_every_n_rounds = persist_every_n_rounds
        self._snapshot_every_n_rounds = snapshot_every_n_rounds
        pass

    def start_controller(self, fl_ctx: FLContext) -> None:
        self.aggregator = self._engine.get_component(self.aggregator_id)

    def stop_controller(self, fl_ctx: FLContext):
        pass

    def control_flow(self, abort_signal: Signal, fl_ctx: FLContext) -> None:
        fl_ctx.set_prop(key="CURRENT_ROUND", value=0)

        get_local_average_task = Task(
            name="get_local_average_and_count",
            data=Shareable(),
            props={},
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
        
    

        self.log_info(fl_ctx, "Start aggregation.")
        aggr_shareable = self.aggregator.aggregate(fl_ctx)
        self.log_info(fl_ctx, "End aggregation.")
    

        print(f"\n\n{'='*50}\nAggregated result: {aggr_shareable}\n{'='*50}\n\n")


    def _accept_site_result(self, client_task: ClientTask, fl_ctx: FLContext) -> bool:
        accepted = self.aggregator.accept(client_task.result, fl_ctx)
        return accepted

    def process_result_of_unknown_task(self, task: Task, fl_ctx: FLContext) -> None:
        pass