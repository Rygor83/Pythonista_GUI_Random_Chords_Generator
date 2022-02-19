import random
from musthe import *
import ui

screen_width = ui.get_screen_size().width

tv_notes = ui.TableView()
tv_notes.border_width = 1
tv_notes.x = 0
tv_notes.y = 0
tv_notes.width = screen_width / 2
tv_notes.height = 150


tv_alter = ui.TableView()
tv_alter.border_width = 1
tv_alter.x = screen_width / 2
tv_alter.y = 0
tv_alter.width = screen_width / 2
tv_alter.height = 150


# Button: convert
bt_generator = ui.Button()
bt_generator.border_width = 4
bt_generator.title = 'Convert'
bt_generator.x = 0
bt_generator.y = 155
bt_generator.width = screen_width
bt_generator.height = 50
bt_generator.font = ('verdana',25)
bt_generator.corner_radius = 20

# TextView: amount about conversion
txtv_info = ui.TextView()
txtv_info.x = 0
txtv_info.y = 210
txtv_info.width = screen_width
txtv_info.height = 250
txtv_info.editable = False
txtv_info.font = ('verdana', 18)
txtv_info.border_width = 1

class MyClass(ui.View):
	
	# определяем ноты
	notes = []
	all_notes = Note('C').all()

	for note in all_notes:
		if note.accidental != '#':
			notes.append(str(note))
	
	data_src_notes = ui.ListDataSource(notes)
	
	# определяем знаки альтерации
	alter = ['all','b','#']
	
	data_src_alter = ui.ListDataSource(alter)
	
	

	
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.table1_selection = None
		self.bg_color = 'lightyellow'
		self.make_view()
		
	def make_view(self):
		self.add_subview(tv_notes)
		self.add_subview(tv_alter)
		self.add_subview(bt_generator)
		self.add_subview(txtv_info)
		
		# Actions
		tv_notes.action = self.data_src_notes
		
		tv_notes.data_source = tv_notes.delegate = self.data_src_notes
		
		tv_alter.action = self.data_src_alter
		
		tv_alter.data_source = tv_alter.delegate = self.data_src_alter
		
		bt_generator.action = self.fn_generate

		
	def fn_date_selected(self, sender):
		self.date = sender.date
		
	def fn_generate(self, sender):
		
		notes = Note('C').all()

		chords = []

		for note in notes:
			if note.accidental != '#':
				chords.append(str(Chord(note, chord_type='maj')))

		txtv_info.text = ', '.join(random.sample(chords, 12))


v = MyClass(name='Chord generator')
v.present('full_screen')
