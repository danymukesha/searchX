import plotly.graph_objects as go

class GenomeBrowser:
    def render(self, chrom: str, start: int, end: int):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[start, end], y=[0, 1], mode="lines"))
        return fig.to_html()
