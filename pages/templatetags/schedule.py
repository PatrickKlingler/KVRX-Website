#https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/

from django.template import Library
from shows.models import Show

register = Library()

@register.filter
def get_range( value ):
	return range( value )

@register.filter
def populate_hour(hour):
	output = ""
	for i in range(0, 7):
		tag_inserted = False
		for show in Show.objects.all():
			if show.get_start_time_string() == hour and show.get_day_num() == i:
				affected_rows = show.get_duration() * 2
				output += """
				<td rowspan="%s">
					<div>
						<h4><a href="/show/%s">%s</a></h4>
						<h5><a href="/dj/%s">%s</a></h5>
					</div>
				</td>
				""" % (affected_rows, show.show_name, show.show_name, show.dj.dj, show.dj.dj)
				tag_inserted = True
			elif not tag_inserted:
				output += "<td></td>"
				tag_inserted =True
	return output