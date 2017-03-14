# -*- coding: utf-8 -*-
from bokeh.plotting import figure, output_file,show

import pygal
import pandas as pd
import numpy as np
from datetime import date,datetime
from pygal.style import Style
from bokeh.charts import Bar, output_file, show
from bokeh.charts.attributes import cat, color
from bokeh.charts.operations import blend
#from enum import Enum



df_china = pd.read_csv('Employment_process_China.csv')
df_china.head()


# #Bokeh line chart
# #df=df_from_json(df_china)
x=pd.date_range('1991-10-01',periods=300,freq='M')
y1=df_china['China_EB1']
y2=df_china['China_EB2']
y3=df_china['China_EB3']


# #DOT
# output_file('China_EB_Waiting_time.html')
# p=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
# #p.line(x,y1,legend='EB1',line_color='orange')
# p.circle(x,y1,legend='EB1',fill_color='orange',line_color='orange')
# #p.line(x,y2,legend='EB2',line_color='blue')
# p.circle(x,y2,legend='EB2',fill_color='blue',line_color='blue')
# #p.line(x,y3,legend='EB3',line_color='green')
# p.circle(x,y3,legend='EB3',fill_color='green',line_color='green')
# show(p)
df_india = pd.read_csv('Employment_process_India.csv')
df_india.head()
# #df=df_from_json(df_india)
#x=pd.date_range('1991-10-01',periods=300,freq='M')
y4=df_india['India_EB1']
y5=df_india['India_EB2']
y6=df_india['India_EB3']

# #area
# #data = dict(zip(x,y4))

# #p2 = Area(data,tools = 'pan,box_zoom,reset,save,xwheel_zoom',title = "India EB1-3 Waiting Time (Month)",legend="top_left", xlabel="Year/Month",ylabel="Waiting time (month)")
# output_file('India_EB_Waiting_time.html')
# #p2 = Bar(df_india, values='EB1_month_diff',label='Year/Month',title='India EB1-3 Waiting Time (Month)', legend='top_right')
# p2=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
# p2.line(x,y4,legend='EB1',line_color='orange')
# #p2.circle(x,y4,legend='EB1',fill_color='green',line_color='green')
# p2.line(x,y5,legend='EB2',line_color='blue')
# #p2.circle(x,y5,legend='EB2',fill_color='blue',line_color='blue')
# p2.line(x,y6,legend='EB3',line_color='green')
# #p2.circle(x,y6,legend='EB3',fill_color='orange',line_color='orange')
# show(p2)

# # x1=range(1, 300)
# # bar=Bar(df,values=blend('EB1_month_diff','EB2_month_diff','EB3_month_diff',name='EB',labels_name='EB1-3'),stack=cat(columns='EB1-3', sort=False),label=cat(columns='Current_year', sort=False),color=color(columns='EB1-3', palette=['SaddleBrown', 'Silver', 'Goldenrod'],
# #                       sort=False),title = 'India EB1-3 Waiting Time (Month)')
# # show(bar)


# output_file('India_China_EB1.html')
# p3=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
# p3.line(x,y1,legend='China EB1',line_color='green')
# #p3.circle(x,y1,legend='China EB1',fill_color='green',line_color='green')
# p3.line(x,y4,legend='India EB1',line_color='blue')
# #p3.circle(x,y4,legend='India EB1',fill_color='blue',line_color='blue')
# show(p3)

# output_file('India_China_EB2.html')
# p4=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
# p4.line(x,y2,legend='China EB2',line_color='green')
# #p4.circle(x,y2,legend='China EB2',fill_color='green',line_color='green')
# p4.line(x,y5,legend='India EB2',line_color='blue')
# #p4.circle(x,y5,legend='India EB2',fill_color='blue',line_color='blue')
# show(p4)

# output_file('India_China_EB3.html')
# p5=figure(plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',x_axis_label='Month', y_axis_label='Waiting time (Months)',x_axis_type="datetime")
# p5.line(x,y3,legend='China EB3',line_color='green')
# #p5.circle(x,y3,legend='China EB3',fill_color='green',line_color='green')
# p5.line(x,y6,legend='India EB3',line_color='blue')
# #p5.circle(x,y6,legend='India EB3',fill_color='blue',line_color='blue')
# show(p5)


#trying stacked bar chart pygal
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  # foreground='#53E89B',
  # foreground_strong='#53A0E8',
  # foreground_subtle='#630C0D',
  # opacity='.6',
  # opacity_hover='.9',
  # transition='400ms ease-in',
  colors=( '#800000', '#D2691E','#DEB887'))
bar_chart = pygal.StackedBar(style=custom_style)
bar_chart.print_labels = True
bar_chart.x_title='Month'
bar_chart.y_title='Waiting time (Months)'
bar_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), x)
#bar_chart.title = 'India EB1-3 Waiting Time (Month)'
#bar_chart.x_labels = range(1, 300)
bar_chart.add('EB1', y1)
bar_chart.add('EB2', y2)
bar_chart.add('EB3', y3)
bar_chart.render_to_file('hiddenGraph_0.svg')

#trying stacked bar chart pygal
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  # foreground='#53E89B',
  # foreground_strong='#53A0E8',
  # foreground_subtle='#630C0D',
  # opacity='.6',
  # opacity_hover='.9',
  # transition='400ms ease-in',
  colors=( '#800000', '#D2691E','#DEB887'))
bar_chart = pygal.StackedBar(style=custom_style)
bar_chart.print_labels = True
bar_chart.x_title='Month'
bar_chart.y_title='Waiting time (Months)'
bar_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), x)
#bar_chart.title = 'India EB1-3 Waiting Time (Month)'
#bar_chart.x_labels = range(1, 300)
bar_chart.add('EB1', y4)
bar_chart.add('EB2', y5)
bar_chart.add('EB3', y6)
bar_chart.render_to_file('hiddenGraph_1.svg')


#trying stacked bar chart pygal
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  # foreground='#53E89B',
  # foreground_strong='#53A0E8',
  # foreground_subtle='#630C0D',
  # opacity='.6',
  # opacity_hover='.9',
  # transition='400ms ease-in',
  colors=( '#800000', '#D2691E'))
bar_chart = pygal.StackedBar(style=custom_style)
bar_chart.print_labels = True
bar_chart.x_title='Month'
bar_chart.y_title='Waiting time (Months)'
bar_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), x)
#bar_chart.title = 'India EB1-3 Waiting Time (Month)'
#bar_chart.x_labels = range(1, 300)
bar_chart.add('China_EB1', y1)
bar_chart.add('China_EB1', y4)
bar_chart.render_to_file('hiddenGraph_2.svg')

#trying stacked bar chart pygal
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  # foreground='#53E89B',
  # foreground_strong='#53A0E8',
  # foreground_subtle='#630C0D',
  # opacity='.6',
  # opacity_hover='.9',
  # transition='400ms ease-in',
  colors=( '#800000', '#D2691E'))
bar_chart = pygal.StackedBar(style=custom_style)
bar_chart.print_labels = True
bar_chart.x_title='Month'
bar_chart.y_title='Waiting time (Months)'
bar_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), x)
#bar_chart.title = 'India EB1-3 Waiting Time (Month)'
#bar_chart.x_labels = range(1, 300)
bar_chart.add('China_EB1', y2)
bar_chart.add('China_EB1', y5)
bar_chart.render_to_file('hiddenGraph_3.svg')

#trying stacked bar chart pygal
custom_style = Style(
  background='transparent',
  plot_background='transparent',
  # foreground='#53E89B',
  # foreground_strong='#53A0E8',
  # foreground_subtle='#630C0D',
  # opacity='.6',
  # opacity_hover='.9',
  # transition='400ms ease-in',
  colors=( '#800000', '#D2691E'))
bar_chart = pygal.StackedBar(style=custom_style)
bar_chart.print_labels = True
bar_chart.x_title='Month'
bar_chart.y_title='Waiting time (Months)'
bar_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), x)
#bar_chart.title = 'India EB1-3 Waiting Time (Month)'
#bar_chart.x_labels = range(1, 300)
bar_chart.add('China_EB1', y3)
bar_chart.add('China_EB1', y6)
bar_chart.render_to_file('hiddenGraph_4.svg')


df_ci = pd.read_csv('China_vs_India.csv')
df_ci.head()
bar=Bar(df_china,
          values=blend('China_EB1', 'China_EB2', 'China_EB3', name='EB1-3', labels_name='EB'),
          label=cat(columns='Date', sort=False),
          stack=cat(columns='EB', sort=False),
          color=color(columns='EB', palette=['SaddleBrown', 'Silver', 'Goldenrod'],
                      sort=False),
          legend='top_right',
          plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',xlabel='Month', ylabel='Waiting time (Months)',xscale='categorical',
          tooltips=[('EB', '@EB'), ('Date', '@Date')]
          )
bar.xaxis.visible = None
output_file("China.html" )
show(bar)

bar=Bar(df_india,
          values=blend('India_EB1', 'India_EB2', 'India_EB3', name='EB1-3', labels_name='EB'),
          label=cat(columns='Date', sort=False),
          stack=cat(columns='EB', sort=False),
          color=color(columns='EB', palette=['SaddleBrown', 'Silver', 'Goldenrod'],
                      sort=False),
          legend='top_right',
          plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',xlabel='Month', ylabel='Waiting time (Months)',xscale="categorical",
          tooltips=[('EB', '@EB'), ('Date', '@Date')]
          )
output_file("India.html" )
show(bar)

bar=Bar(df_ci,
          values=blend('India_EB1', 'China_EB1', name='EB1', labels_name='EB1ci'),
          label=cat(columns='Date', sort=False),
          stack=cat(columns='EB1ci', sort=False),
          color=color(columns='EB1ci', palette=['green','blue'],
                      sort=False),
          legend='top_right',
          plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',xlabel='Month', ylabel='Waiting time (Months)',xscale="categorical",
          tooltips=[('EB1ci', '@EB1ci'), ('Date', '@Date')]
          )
output_file("EB1.html" )
show(bar)

bar=Bar(df_ci,
          values=blend('India_EB2', 'China_EB2', name='EB2', labels_name='EB2ci'),
          label=cat(columns='Date', sort=False),
          stack=cat(columns='EB2ci', sort=False),
          color=color(columns='EB2ci', palette=['green','blue'],
                      sort=False),
          legend='top_right',
          plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',xlabel='Month', ylabel='Waiting time (Months)',xscale="categorical",
          tooltips=[('EB2ci', '@EB2ci'), ('Date', '@Date')]
          )
output_file("EB2.html" )
show(bar)

bar=Bar(df_ci,
          values=blend('India_EB3', 'China_EB3', name='EB3', labels_name='EB3ci'),
          label=cat(columns='Date', sort=False),
          stack=cat(columns='EB3ci', sort=False),
          color=color(columns='EB3ci', palette=['green','blue'],
                      sort=False),
          legend='top_right',
          plot_width=900,tools = 'pan,box_zoom,reset,save,xwheel_zoom',xlabel='Month', ylabel='Waiting time (Months)',xscale="categorical",
          tooltips=[('EB3ci', '@EB3ci'), ('Date', '@Date')]
          )
output_file("EB3.html" )
show(bar)
