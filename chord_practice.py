import random
from musthe import *
import ui
from collections import OrderedDict

# Chord notation: https://en.m.wikipedia.org/wiki/Chord_notation#Triads


# --------------------------------
#    CLASSES FOR chord types
# --------------------------------
#             TRIADS
# --------------------------------
class Major():

	sym_short = 'M'
	sym = 'maj'
	sym_default = ''
	symbols = ['', 'maj', 'M']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Minor():

	sym_short = 'm'
	sym = 'min'
	sym_default = 'm'
	symbols = ['-', 'min', 'm']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Augmented():

	sym_short = '+'
	sym = 'aug'
	sym_default = 'aug'
	symbols = ['aug', 'M#5', 'M+5']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Diminished():

	sym_short = '°'
	sym = 'dim'
	sym_default = 'dim'
	symbols = ['dim', 'mb5', 'm°5']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


# --------------------------------
#             7th
# --------------------------------
class Major7():

	triangle = chr(9651)

	sym_short = 'M7'
	sym = 'maj7'
	sym_default = ''
	symbols = ['maj7', 'M7', triangle]

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Minor7():

	sym_short = 'm7'
	sym = 'min7'
	sym_default = 'm7'
	symbols = ['min7', 'm7', '-7']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Dominant7():

	sym_short = '7'
	sym = 'dom7'
	sym_default = '7'
	symbols = ['dom7', '7']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Augimented7():

	sym_short = '+'
	sym = 'aug'
	sym_default = 'aug'
	symbols = ['M#5', 'M+5']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Diminished7():

	sym_short = '°'
	sym = 'dim'
	sym_default = 'dim'
	symbols = ['mb5', 'm°5']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


obj = {
	'M': Major(),
	'm': Minor(),
	'+': Augmented(),
	'°': Diminished(),
	'M7': Major7(),
	'm7': Minor7(),
	'7': Dominant7()
}

# --------------------------------
#       USER INTERFACE
# --------------------------------

screen_width = ui.get_screen_size().width
screen_height = ui.get_screen_size().height

tv_height = 125
tv_x_pos = screen_width / 3
tv_y_pos = 0

# Table view: Accidentals
tv_alter = ui.TableView()
tv_alter.border_width = 0
tv_alter.x = 0 * tv_x_pos
tv_alter.y = tv_y_pos
tv_alter.width = screen_width / 3
tv_alter.height = tv_height

# Table view: Chord type
tv_type = ui.TableView()
tv_type.border_width = 0
tv_type.x = 1 * tv_x_pos
tv_type.y = tv_y_pos
tv_type.width = screen_width / 3
tv_type.height = tv_height
tv_type.allows_multiple_selection = True

# Table view: Chord view
tv_view = ui.TableView()
tv_view.border_width = 0
tv_view.x = 2 * tv_x_pos
tv_view.y = 0
tv_view.width = screen_width / 3
tv_view.height = tv_height

# Button: generate chord
bt_height = 40
bt_x_pos = 0
bt_y_pos = tv_height + 5

bt_generator = ui.Button()
bt_generator.border_width = 4
bt_generator.title = 'Generate'
bt_generator.x = bt_x_pos
bt_generator.y = bt_y_pos
bt_generator.width = screen_width
bt_generator.height = bt_height
bt_generator.font = ('verdana', 25)
bt_generator.corner_radius = 10

# TextView: amount about conversion
txtv_height = screen_height - tv_height - tv_height - bt_height + 15  #280
txtv_x_pos = 0
txtv_y_pos = bt_y_pos + bt_height + 5

txtv_info = ui.TextView()
txtv_info.alignment = ui.ALIGN_CENTER
txtv_info.border_width = 0
txtv_info.x = txtv_x_pos
txtv_info.y = txtv_y_pos
txtv_info.width = screen_width
txtv_info.height = txtv_height
txtv_info.editable = False
txtv_info.font = ('verdana-bold', 30)


class tvDelegateType(object):
	def __init__(self, items):
		self.items = items
		self.selected_items = []
		self.currentNumLines = len(items)
		self.currentTitle = 'Type'

	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		self.selected_items.append(self.items[row])

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		self.selected_items.remove(self.items[row])


class tvDataSourceAlter(object):
	def __init__(self):
		self.i = 1
	
	def tableview_number_of_sections(self, tableview):
		# Return the number of sections (defaults to 1)
		return 1

	def tableview_number_of_rows(self, tableview, section):
		# Return the number of rows in the section
		return 3

	def tableview_cell_for_row(self, tableview, section, row):
		# Create and return a cell for the given section/row
		self.i = self.i + 1
		
		cell = ui.TableViewCell()
		cell.text_label.text = str(row)
		return cell
		

	def tableview_title_for_header(self, tableview, section):
		# Return a title for the given section.
		# If this is not implemented, no section headers will be shown.
		return 'Accedentals'
		
	def fill(self, tableview, data):
		for section in data:
			self.tableview_title_for_header(tableview, section)
			
			for ind, row in enumerate(data[section]):
				self.tableview_cell_for_row(tableview, section, row)

class ChordGenerator(ui.View):

	selected_note = ""
	selected_alter = ""
	selected_type = ""
	selected_types = []
	selected_view = ""

	types = []

	# определяем ноты
	notes = []
	all_notes = Note('C').all()

	for note in all_notes:
		notes.append(str(note))

	data_src_notes = ui.ListDataSource(notes)

	# ListDataSource for accidentals
	alter = {'Accidentals':['b', '#', 'all']}
	
	
	# data_src_alter = ui.ListDataSource(alter)
	
	data_src_alter =  tvDataSourceAlter()
	
	data_src_alter.fill(tv_alter, alter)
	
	tv_alter.data_source = data_src_alter
	tv_alter.delegate = data_src_alter
	
	

	# определяем типы аккордов
	for key, item in Chord(Note('C')).aliases.items():
		types.append(key)

	data_src_type = ui.ListDataSource(types)

	# определяем как будет выглядеть аккорд
	chord_views = ['Random', 'Default', 'Musthe']

	data_src_view = ui.ListDataSource(chord_views)

	#-------------------------

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.table1_selection = None
		self.bg_color = 'lightyellow'
		self.make_view()

	def make_view(self):
		self.add_subview(tv_alter)
		self.add_subview(tv_type)
		self.add_subview(tv_view)
		self.add_subview(bt_generator)
		self.add_subview(txtv_info)

		# Actions
		self.data_src_alter.action = self.fn_alter_selected

		tv_type.data_source = self.data_src_type

		tv_type.delegate = tvDelegateType(self.types)

		# View
		self.data_src_view.action = self.fn_view_selected

		tv_view.data_source = tv_view.delegate = self.data_src_view

		# Button: gnerate
		bt_generator.action = self.fn_generate

	def fn_note_selected(self, sender):
		self.selected_note = sender.items[sender.selected_row]

	def fn_alter_selected(self, sender):
		self.selected_alter = sender.items[sender.selected_row]

	def fn_view_selected(self, sender):
		self.selected_view = sender.items[sender.selected_row]

	def fn_generate(self, sender):

		notes = Note('C').all()
		chords = []
		all_chords = []
		new_chord = ''

		if self.selected_alter == '':
			txtv_info.text = 'Select accidentals'

		elif tv_type.delegate.selected_items == []:
			txtv_info.text = 'Select chord type'

		elif self.selected_view == '':
			txtv_info.text = 'Select output type'

		else:

			for note in notes:
				for item_type in tv_type.delegate.selected_items:

					if self.selected_alter == 'all' or note.accidental == self.selected_alter or note.accidental == '':

						new_chord = str(Chord(note, chord_type=item_type))

						# заменяем обозначения
						if self.selected_view == 'Random':

							t = obj[item_type]

							new_chord = t.replace(new_chord)

						elif self.selected_view == 'Default':

							t = obj[item_type]
							new_chord = t.replace_default(new_chord)
						all_chords.append(new_chord)

			txtv_info.text = ', '.join(random.sample(all_chords, len(all_chords)))


# --------------------------------
# MAIN
# -------------------------------
v = ChordGenerator(name='CHORD GENERATOR')
v.present('full_screen')
