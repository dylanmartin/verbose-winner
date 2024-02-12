from nvflare.apis.impl.controller import ClientTask, Controller, Task
from nvflare.apis.fl_context import FLContext
from nvflare.apis.signal import Signal

class ssr_csv(Controller):
    def __init__(
        self
    ):
        pass
    def start_controller(self, fl_ctx: FLContext) -> None:
        pass
    def stop_controller(self, fl_ctx: FLContext):
        pass
    def control_flow(self, abort_signal: Signal, fl_ctx: FLContext) -> None:
        pass