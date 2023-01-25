import pandas as pd
import plotly.express as px
import streamlit
from plotly.graph_objs import graph_objs
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from umap import UMAP


class PlotMaster:
    def __init__(
        self, input_data, labels: list[str], order: list[int | float], color_map: dict
    ):
        self.input_data = input_data
        self.labels = labels
        self.order = order
        self.color_map = color_map

    def plot_interactive(self, data, layout):
        return graph_objs.Figure(data=data, layout=layout)

    def order_labels(self):
        ordered_labels = []
        for index in self.order:
            ordered_labels.append(self.labels[int(index)])
        return ordered_labels

    def df_to_plotly(
        self,
        df: pd.DataFrame,
        desired_columns: list,
    ):
        df = df.reindex(self.order)
        df = df[desired_columns].T
        return {"z": df.values, "x": self.order_labels(), "y": df.index.tolist()}

    def plot_pca(self):
        pca = PCA(2).fit_transform(self.input_data)
        print(pca)
        fig = px.scatter(pca, x=0, y=1, color=self.color_map, hover_name=self.labels)
        return fig

    def plot_pca_3d(self):
        pca = PCA(3).fit_transform(self.input_data)
        fig = px.scatter_3d(
            pca, x=0, y=1, z=2, color=self.color_map, hover_name=self.labels
        )
        return fig

    def plot_all_dimensions(self):
        features = self.input_data.columns
        fig = px.scatter_matrix(
            self.input_data,
            dimensions=features,
            color=self.color_map,
            hover_name=self.labels,
        )
        fig.update_traces(diagonal_visible=True)
        return fig

    def plot_tsne(self):
        tsne = TSNE(n_components=2, random_state=0, perplexity=5).fit_transform(
            self.input_data
        )
        fig = px.scatter(
            tsne,
            x=0,
            y=1,
            color=self.color_map,
            hover_name=self.labels,
            labels={"color": "states"},
        )
        return fig

    def plot_tsne_3D(self):
        tsne = TSNE(n_components=3, random_state=0, perplexity=5).fit_transform(
            self.input_data
        )
        fig = px.scatter_3d(
            tsne,
            x=0,
            y=1,
            z=2,
            color=self.color_map,
            hover_name=self.labels,
            labels={"color": "states"},
        )
        return fig

    def plot_umap(self):
        umap = UMAP(n_components=2, init="random", random_state=0).fit_transform(
            self.input_data
        )
        fig = px.scatter(
            umap,
            x=0,
            y=1,
            color=self.color_map,
            hover_name=self.labels,
            labels={"color": "states"},
        )
        return fig

    def plot_umap_3D(self):
        umap = UMAP(n_components=3, init="random", random_state=0).fit_transform(
            self.input_data
        )
        fig = px.scatter_3d(
            umap,
            x=0,
            y=1,
            z=2,
            color=self.color_map,
            hover_name=self.labels,
            labels={"color": "states"},
        )
        return fig

    def plot_selected_features_streamlit(self):
        desired_columns = streamlit.multiselect(
            "Choose 2 features to plot.", self.input_data.columns
        )
        if len(desired_columns) != 2:
            streamlit.write("Please choose 2 features to plot.")
        else:
            to_plot = self.input_data[desired_columns]
            fig = px.scatter(
                to_plot,
                x=to_plot.columns[0],
                y=to_plot.columns[1],
                color=self.color_map,
                hover_name=self.labels,
                labels={"color": "states"},
            )
            return fig

    def plot_selected_features(self, desired_columns):
        to_plot = self.input_data[desired_columns]
        fig = px.scatter(
            to_plot,
            x=to_plot.columns[0],
            y=to_plot.columns[1],
            color=self.color_map,
            hover_name=self.labels,
            labels={"color": "states"},
        )
        return fig
