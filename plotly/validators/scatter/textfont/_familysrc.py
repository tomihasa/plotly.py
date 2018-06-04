import _plotly_utils.basevalidators


class FamilysrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='familysrc',
        parent_name='scatter.textfont',
        **kwargs
    ):
        super(FamilysrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )