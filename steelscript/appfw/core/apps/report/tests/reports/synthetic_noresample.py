from steelscript.appfw.core.apps.datasource.modules.analysis import AnalysisTable
from steelscript.appfw.core.apps.datasource.models import Column

from steelscript.appfw.core.apps.report.models import Report, Section
from steelscript.appfw.core.apps.report.modules import raw
from steelscript.appfw.core.apps.datasource.forms import fields_add_time_selection, fields_add_resolution
from steelscript.appfw.core.libs.fields import Function

# Report
from steelscript.appfw.core.apps.report.tests.reports import synthetic_functions as funcs

report = Report(title='Synthetic No Resampling' )
report.save()

# Section
section = Section(report=report, title='Section 0')
section.save()

# Table
a = AnalysisTable.create('test-synthetic-noresampling', tables={},
                         function=Function(funcs.analysis_generate_data,
                                           params={'source_resolution': 60}))
fields_add_time_selection(a)
fields_add_resolution(a)

a.add_column('time', 'Time', iskey=True, datatype='time')
a.add_column('value', 'Value')

raw.TableWidget.create(section, a, 'Table')