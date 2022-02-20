import random
from musthe import *
import ui

screen_width = ui.get_screen_size().width

tv_notes = ui.TableView()
tv_notes.border_width = 0
tv_notes.x = 0
tv_notes.y = 0
tv_notes.width = screen_width / 3
tv_notes.height = 150

tv_alter = ui.TableView()
tv_alter.border_width = 0
tv_alter.x = screen_width / 3
tv_alter.y = 0
tv_alter.width = screen_width / 3
tv_alter.height = 150

tv_type = ui.TableView()
tv_type.border_width = 0
tv_type.x = 2 * screen_width / 3
tv_type.y = 0
tv_type.width = screen_width / 3
tv_type.height = 150

# Button: convert
bt_generator = ui.Button()
bt_generator.border_width = 4
bt_generator.title = 'Generate'
bt_generator.x = 0
bt_generator.y = 155
bt_generator.width = screen_width
bt_generator.height = 50
bt_generator.font = ('verdana', 25)
bt_generator.corner_radius = 20

# TextView: amount about conversion
txtv_info = ui.TextView()
txtv_info.border_width = 0
txtv_info.x = 0
txtv_info.y = 210
txtv_info.width = screen_width
txtv_info.height = 250
txtv_info.editable = False
txtv_info.font = ('verdana', 18)



class MyClass(ui.View):

	selected_note = ""
	selected_alter = ""
	selected_type = ""

	types = []

	# определяем ноты
	notes = []
	all_notes = Note('C').all()

	for note in all_notes:
		#if note.accidental != '#':
		notes.append(str(note))

	data_src_notes = ui.ListDataSource(notes)

	# определяем знаки альтерации
	alter = ['all', 'b', '#']

	data_src_alter = ui.ListDataSource(alter)

	# определяем типы аккордов
	for key, item in Chord(Note('C')).aliases.items():
		types.append(key)

	data_src_type = ui.ListDataSource(types)

	#-------------------------

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.table1_selection = None
		self.bg_color = 'lightyellow'
		self.make_view()

	def make_view(self):
		self.add_subview(tv_notes)
		self.add_subview(tv_alter)
		self.add_subview(tv_type)
		self.add_subview(bt_generator)
		self.add_subview(txtv_info)

		# Actions
		self.data_src_notes.action = self.fn_note_selected

		tv_notes.data_source = tv_notes.delegate = self.data_src_notes

		self.data_src_alter.action = self.fn_alter_selected

		tv_alter.data_source = tv_alter.delegate = self.data_src_alter

		self.data_src_type.action = self.fn_type_selected

		tv_type.data_source = tv_type.delegate = self.data_src_type

		bt_generator.action = self.fn_generate

	def fn_note_selected(self, sender):
		self.selected_note = sender.items[sender.selected_row]

	def fn_alter_selected(self, sender):
		self.selected_alter = sender.items[sender.selected_row]

	def fn_type_selected(self, sender):
		self.selected_type = sender.items[sender.selected_row]

	def fn_generate(self, sender):

		notes = Note('C').all()

		chords = []

		for note in notes:
			if note.accidental == self.selected_alter or note.accidental == '':
				chords.append(str(Chord(note, chord_type=self.selected_type)))

		txtv_info.text = ', '.join(random.sample(chords, len(chords)))


v = MyClass(name='CHORD GENERATOR')
v.present('full_screen')

