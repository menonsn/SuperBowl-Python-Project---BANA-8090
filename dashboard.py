{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import dash\n",
    "import dash_core_components as dcc\n",
    "import dash_html_components as html\n",
    "import pandas as pd\n",
    "\n",
    "external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']\n",
    "\n",
    "app = dash.Dash(__name__, external_stylesheets=external_stylesheets)\n",
    "\n",
    "df = pd.read_csv('super_bowls.csv')\n",
    "\n",
    "\n",
    "colors = {\n",
    "    'background': '#111111',\n",
    "    'text': '#7FDBFF'\n",
    "}\n",
    "\n",
    "\n",
    "app.layout = html.Div(children=[\n",
    "    html.H1(children='Web Dashboard for Super Bowl dataset'),\n",
    "    html.Div(children='''Scatter plot of the Attendance and Winners of each Super Bowl Event!'''),\n",
    "    dcc.Graph(\n",
    "        id='attendance_winner',\n",
    "        figure={\n",
    "            'data': [\n",
    "                dict(\n",
    "                    x=df[df['super_bowl'] == i]['attendance'],\n",
    "                    y=df[df['super_bowl'] == i]['team_winner'],\n",
    "                    text=df[df['super_bowl'] == i]['combined_pts'],\n",
    "                    mode='markers',\n",
    "                    opacity=0.7,\n",
    "                    marker={\n",
    "                        'size': 15,\n",
    "                        'line': {'width': 0.5, 'color': 'white'}\n",
    "                    },\n",
    "                    name=i\n",
    "                ) for i in df.super_bowl.unique()\n",
    "            ],\n",
    "            'layout': dict(\n",
    "                xaxis={'title': 'Attendance at every Super Bowl'},\n",
    "                yaxis={'title': 'Super Bowl Number and all Winners'},\n",
    "                margin={'l': 170, 'b': 40, 't': 10, 'r': 10},\n",
    "                legend={'x': 0, 'y': 1},\n",
    "                hovermode='closest'\n",
    "            )\n",
    "        }\n",
    "    )\n",
    "    \n",
    "])\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
