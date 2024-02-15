from remote_1 import remote_1

class Ssr_csv_aggregator(Aggregator):
    def __init__(
        self,
    ):
        super().__init__()
        self.stored_data = {}

    
    def accept(self, shareable: Shareable, fl_ctx: FLContext) -> bool:

        ## add the data in this shareable to the list of shareables for this contribution round
        contribution_round = fl_ctx.get_prop(key=ReservedKey.CURRENT_ROUND, default="?")
        contributor_name = shareable.get_peer_prop(key=ReservedKey.IDENTITY_NAME, default="?")
        
        if(contribution_round not in self.stored_data):
            self.stored_data[contribution_round] = []
        
        self.stored_data[contribution_round][contributor_name]
        self.stored_data[contribution_round][contributor_name] = shareable["result"]
        ## no checking at this point, just accept
        return True

    
    def aggregate(self, fl_ctx: FLContext) -> Shareable:
        contribution_round = fl_ctx.get_prop(key=ReservedKey.CURRENT_ROUND, default="?")
        if(contribution_round == 1):
            remote_1(self.stored_data[contribution_round])
        if(contribution_round == 2):
            remote_2(self.stored_data[contribution_round])
            
        
        
        pass
        