from nvflare.apis.dxo import DXO, DataKind, MetaKey, from_shareable
from nvflare.apis.executor import Executor
from nvflare.apis.fl_constant import FLContextKey, ReturnCode
from nvflare.apis.fl_context import FLContext
from nvflare.apis.shareable import Shareable, make_reply
from nvflare.apis.signal import Signal
from nvflare.app_common.abstract.model import ModelLearnable
from nvflare.app_common.app_constant import AppConstants
from nvflare.security.logging import secure_format_exception

taskNames = {
    "local_1": "local_1",
    "local_2": "local_2"
}
class ssr_csv_executor(Executor):
    def execute(
        self,
        task_name: str,
        shareable: Shareable,
        fl_ctx: FLContext,
        abort_signal: Signal,
    ) -> Shareable:
        
        if task_name == taskNames["local_1"]:
            return self.local_1(shareable, fl_ctx, abort_signal)
        if task_name == taskNames["local_2"]:
            return self.local_2(shareable, fl_ctx, abort_signal)
        pass