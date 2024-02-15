from nvflare.apis.shareable import Shareable
from nvflare.apis.fl_context import FLContext
from nvflare.app_common.abstract.aggregator import Aggregator

from get_global_average import get_global_average

class AverageAggregator(Aggregator):
    def __init__(
        self,
    ):
        super().__init__()
        self.stored_data = {}
    """
    {
        [round_number][site_name] = [data]
    }
    
    site data will be a dict containing average and count
    """

    def accept(self, shareable: Shareable, fl_ctx: FLContext) -> bool:

        # add the data in this shareable to the list of shareables for this contribution round
        contribution_round = fl_ctx.get_prop(
            key=ReservedKey.CURRENT_ROUND, default="?")
        contributor_name = shareable.get_peer_prop(
            key=ReservedKey.IDENTITY_NAME, default="?")

        if (contribution_round not in self.stored_data):
            self.stored_data[contribution_round] = []

        self.stored_data[contribution_round][contributor_name]
        self.stored_data[contribution_round][contributor_name] = shareable["result"]
        # no checking at this point, just accept
        return True

    def aggregate(self, fl_ctx: FLContext) -> Shareable:
        contribution_round = fl_ctx.get_prop(
            key=ReservedKey.CURRENT_ROUND, default="?")
        # for each site in this round of stored data, calculate the average
        # and store it in a new shareable
        global_average = get_global_average(
            self.stored_data[contribution_round])
        return Shareable({"global_average": global_average})
