from nvflare.apis.dxo import DXO, DataKind, MetaKey, from_shareable
from nvflare.apis.executor import Executor
from nvflare.apis.fl_constant import FLContextKey, ReturnCode
from nvflare.apis.fl_context import FLContext
from nvflare.apis.shareable import Shareable, make_reply
from nvflare.apis.signal import Signal
from nvflare.app_common.abstract.model import ModelLearnable
from nvflare.app_common.app_constant import AppConstants
from nvflare.security.logging import secure_format_exception
from .local_average import get_local_average_and_count

class AverageExecutor(Executor):
    def execute(
        self,
        task_name: str,
        shareable: Shareable,
        fl_ctx: FLContext,
        abort_signal: Signal,
    ) -> Shareable:
        
        print(f"[bold green]\n\nExecutor received task: {task_name}\n\n[/bold green]")
        
        if task_name == "get_local_average_and_count":
            local_average_and_count = get_local_average_and_count()
            outgoing_shareable = Shareable()
            outgoing_shareable["result"] = local_average_and_count
            return outgoing_shareable

