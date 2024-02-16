from nvflare.apis.shareable import Shareable
from nvflare.apis.fl_context import FLContext
from nvflare.app_common.abstract.aggregator import Aggregator
from nvflare.apis.fl_constant import ReservedKey
from .get_global_average import get_global_average

class AverageAggregator(Aggregator):
    def __init__(self):
        super().__init__()
        # Initialize stored_data to hold contributions per round and contributor
        self.stored_data = {}  # Structure: {round_number: {contributor_name: data}}

    def accept(self, shareable: Shareable, fl_ctx: FLContext) -> bool:
        """Accepts shareable contributions for aggregation.

        Args:
            shareable: The shareable data from a contributor.
            fl_ctx: The federated learning context.

        Returns:
            bool: True indicating acceptance of the shareable data.
        """
        contribution_round = fl_ctx.get_prop(key="CURRENT_ROUND", default=None)
        contributor_name = shareable.get_peer_prop(key=ReservedKey.IDENTITY_NAME, default=None)

        print(f"Aggregator received contribution from {contributor_name} for round {contribution_round}")
        if contribution_round is None or contributor_name is None:
            return False  # Could log a warning/error here as well

        if contribution_round not in self.stored_data:
            self.stored_data[contribution_round] = {}

        # It's assumed shareable.get("result", {}) correctly fetches the data dict
        self.stored_data[contribution_round][contributor_name] = shareable.get("result", {})
        return True

    def aggregate(self, fl_ctx: FLContext) -> Shareable:
        """Aggregates contributions for the current round into a global average.

        Args:
            fl_ctx: The federated learning context.

        Returns:
            Shareable: A shareable containing the global average.
        """
        contribution_round = fl_ctx.get_prop(key="CURRENT_ROUND", default=None)
        data_for_aggregation = []

        if contribution_round in self.stored_data and self.stored_data[contribution_round]:
            for data in self.stored_data[contribution_round].values():
                data_for_aggregation.append(data)

            global_average = get_global_average(data_for_aggregation)
            outgoing_shareable = Shareable()
            outgoing_shareable["global_average"] = global_average
            
            return outgoing_shareable
        else:
            return Shareable()  # Return an empty Shareable if no data to aggregate

