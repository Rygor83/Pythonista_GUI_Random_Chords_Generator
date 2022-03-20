import random
from musthe import *
import ui

symbols_maj = ['','maj','M']
symbols_min = ['-','min','m']

screen_width = ui.get_screen_size().width

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
bt_height = 50
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
bt_generator.corner_radius = 20

# TextView: amount about conversion
txtv_height = 280
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



class MyClass(ui.View):

	selected_note = ""
	selected_alter = ""
	selected_type = ""
	selected_view = ""

	types = []

	# определяем ноты
	notes = []
	all_notes = Note('C').all()

	for note in all_notes:
		notes.append(str(note))

	data_src_notes = ui.ListDataSource(notes)

	# ListDataSource for accidentals
	alter = ['b', '#', 'all']

	data_src_alter = ui.ListDataSource(alter)

	# определяем типы аккордов
	for key, item in Chord(Note('C')).aliases.items():
		types.append(key)

	data_src_type = ui.ListDataSource(types)
	
	# определяем как будет выглядеть аккорд
	chord_views = ['Random', 'Default', 'No']

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

		tv_alter.data_source = tv_alter.delegate = self.data_src_alter

		self.data_src_type.action = self.fn_type_selected

		tv_type.data_source = tv_type.delegate = self.data_src_type

		# View
		self.data_src_view.action = self.fn_view_selected

		tv_view.data_source = tv_view.delegate = self.data_src_view
		
		# Button: gnerate
		bt_generator.action = self.fn_generate

	def fn_note_selected(self, sender):
		self.selected_note = sender.items[sender.selected_row]

	def fn_alter_selected(self, sender):
		self.selected_alter = sender.items[sender.selected_row]

	def fn_type_selected(self, sender):
		self.selected_type = sender.items[sender.selected_row]
		
	def fn_view_selected(self, sender):
		self.selected_view = sender.items[sender.selected_row]

	def fn_generate(self, sender):
		notes = Note('C').all()
		chords = []
		all_chords = []
		
		if self.selected_alter == '' and self.selected_type == '':
			txtv_info.text = 'Select accidentals and chord type'
			
		elif self.selected_type == '':
			txtv_info.text = 'Select accidentals'
			
		elif self.selected_view == '':
			txtv_info.text = 'Select chord type'
			
		else:

			for note in notes:
				if self.selected_alter == 'all' or note.accidental == self.selected_alter or note.accidental == '':
					chords.append(str(Chord(note, chord_type=self.selected_type)))
					
			# подмена мтандарта
			if self.selected_view == 'Random':
				
				
				for ch in chords:
					sym = random.choice(symbols_maj)
					ch = ch.replace('maj', sym)
					
					all_chords.append(ch)
			elif self.selected_view == 'No':
				for ch in chords:
					sym = ''
					ch = ch.replace('maj', sym)
					
					all_chords.append(ch)
			else:
				all_chords = chords

			
			txtv_info.text = ', '.join(random.sample(all_chords, len(all_chords)))


v = MyClass(name='CHORD GENERATOR')
v.present('full_screen')

