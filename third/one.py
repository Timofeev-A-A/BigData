import plotly
import plotly.express as px


def task_three(data):
    zero = int(data['total'].min() - (data['total'].min() * 0.1))
    zero2 = int(data['total'].max() + (data['total'].max() * 0.05))
    hist = px.bar(data, x="district", y="total", color="total", title="Amount of electors in districts")
    hist.update_layout(
        font_size=16,
        title_font_size=20,
        title_x=0.5
    )
    hist.update_xaxes(
        tickfont=dict(size=14),
        tickangle=270
    )
    hist.update_yaxes(
        tickfont=dict(size=14),
        tickmode='linear',
        range=[zero, zero2],
        dtick=600
    )
    hist.show()


def task_four(data):
    pie = px.pie(data, names="district", values="total", title="Amount of electors in districts")
    pie.update_layout(
        font_size=16,
        title_font_size=20,
        title_x=0.5
    )
    pie.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=14)
    pie.show()


def task_five(data):
    zero = int(data['total'].min() - (data['total'].min() * 0.1))
    zero2 = int(data['total'].max() + (data['total'].max() * 0.05))
    line = px.line(data, x="district", y="total", title="Amount of electors in districts",
                   markers=True)
    line.update_layout(
        font_size=16,
        title_font_size=20,
        title_x=0.5,
        legend=dict(
            yanchor="bottom",
            xanchor="left"
        ),
        showlegend=True
    )
    line.update_xaxes(
        tickfont=dict(size=14),
        tickangle=270,
        showgrid=True,
        gridwidth=1,
        gridcolor='azure'
    )
    line.update_yaxes(
        tickfont=dict(size=14),
        tickmode='linear',
        range=[zero, zero2],
        dtick=600,
        showgrid=True,
        gridwidth=1,
        gridcolor='azure'
    )
    line.update_traces(line=dict(color='crimson'), marker=dict(size=8, color='darkblue', line=dict(width=1, color='black')))
    line.show()


def task_six(data):
    fig = px.box(data, y="total", title="Amount of electors in districts")
    fig.update_layout(
        font_size=16,
        title_font_size=20,
        title_x=0.5
    )
    fig.show()


if __name__ == '__main__':
    df = plotly.data.election()
    print(df.head(20))
    df.info()
    print(df.isna().sum())
    task_three(df)
    task_four(df)
    task_five(df)
    task_six(df)

