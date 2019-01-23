#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Jan 11, 2019 12:32:53 PM EST  platform: Windows NT

import sys
import platform

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from src import PyDrink_support


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = tk.Tk()
    top = PyDrink(root)
    PyDrink_support.init(root, top)
    root.mainloop()


w = None


def create_PyDrink(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = PyDrink(w)
    PyDrink_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_PyDrink():
    global w
    w.destroy()
    w = None


class PyDrink:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        _tabpadding = [root.winfo_screenwidth()*0.08,5]
        font9 = "-family {Segoe UI} -size 12 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1080x720+225+19")
        top.title("PyDrink")
        top.configure(background="#d9d9d9")

        self.images = (

         tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                 KkoNUtRHpYYAADs= '''),

         tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),

         tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )

        self.style.element_create("close", "image", "img_close",
               ("active", "pressed", "!disabled", "img_closepressed"),
               ("active", "alternate", "!disabled",
               "img_closeactive"), border=8, sticky='')

        self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                     {"sticky": "nswe"})])

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.configure('TNotebook.Tab', tabposition="center")
        self.style.configure('TNotebook.Tab', padding=_tabpadding)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.style.map('TNotebook.Tab', padding=
            [('selected', _tabpadding), ('active', _tabpadding)])
        self.notebook = ttk.Notebook(top)
        self.notebook.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.notebook.configure(width=1080)
        self.notebook.configure(takefocus="")
        self.notebook_t0 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t0, padding=3)
        self.notebook.tab(0, text="Inventory", compound="none", underline="-1", state='disabled')
        self.notebook_t0.configure(background="#d9d9d9")
        self.notebook_t0.configure(highlightbackground="#d9d9d9")
        self.notebook_t0.configure(highlightcolor="black")
        self.notebook_t1 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t1, padding=3)
        self.notebook.tab(1, text="Fridge", compound="none", underline="-1")
        self.notebook_t1.configure(background="#d9d9d9")
        self.notebook_t1.configure(highlightbackground="#d9d9d9")
        self.notebook_t1.configure(highlightcolor="black")
        self.notebook_t2 = tk.Frame(self.notebook)
        self.notebook.add(self.notebook_t2, padding=3)
        self.notebook.tab(2, text="Glass", compound="none", underline="-1")
        self.notebook_t2.configure(background="#d9d9d9")
        self.notebook_t2.configure(highlightbackground="#d9d9d9")
        self.notebook_t2.configure(highlightcolor="black")

        self.cnv_list_fridge = tk.Canvas(self.notebook_t1)
        self.cnv_list_fridge.place(relx=0.0, rely=0.015, relheight=0.919
                                   , relwidth=0.635)
        self.cnv_list_fridge.configure(background="#d9d9d9")
        self.cnv_list_fridge.configure(borderwidth="2")
        self.cnv_list_fridge.configure(insertbackground="black")
        self.cnv_list_fridge.configure(relief='ridge')
        self.cnv_list_fridge.configure(selectbackground="#c4c4c4")
        self.cnv_list_fridge.configure(selectforeground="black")
        self.cnv_list_fridge.configure(width=683)

        self.frame_list_fridge = tk.Frame(self.cnv_list_fridge)
        self.frame_list_fridge.place(relx=0.015, rely=0.016, relheight=0.972
                                     , relwidth=0.974)
        self.frame_list_fridge.configure(relief='groove')
        self.frame_list_fridge.configure(borderwidth="2")
        self.frame_list_fridge.configure(relief='groove')
        self.frame_list_fridge.configure(background="#d9d9d9")
        self.frame_list_fridge.configure(width=665)

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.stv_list_fridge = ScrolledTreeView(self.frame_list_fridge)
        self.stv_list_fridge.place(relx=0.015, rely=0.016, relheight=0.971
                                   , relwidth=0.962)
        self.stv_list_fridge.configure(columns="Select")
        self.stv_list_fridge.heading("#0", text="Drink")
        self.stv_list_fridge.heading("#0", anchor="center")
        self.stv_list_fridge.column("#0", width="308")
        self.stv_list_fridge.column("#0", minwidth="20")
        self.stv_list_fridge.column("#0", stretch="1")
        self.stv_list_fridge.column("#0", anchor="w")
        self.stv_list_fridge.heading("Select", text="Select")
        self.stv_list_fridge.heading("Select", anchor="center")
        self.stv_list_fridge.column("Select", width="309")
        self.stv_list_fridge.column("Select", minwidth="20")
        self.stv_list_fridge.column("Select", stretch="1")
        self.stv_list_fridge.column("Select", anchor="center")
        self.notebook_t1.bind('<Visibility>', lambda e: PyDrink_support.ntb_open_fridge(e, self.stv_list_fridge,
                                                                                        self.txtbx_fridge_selected,
                                                                                        self.lbl_add_glass_success))

        self.cnv_select_fridge = tk.Canvas(self.notebook_t1)
        self.cnv_select_fridge.place(relx=0.632, rely=0.015, relheight=0.919
                                     , relwidth=0.365)
        self.cnv_select_fridge.configure(background="#d9d9d9")
        self.cnv_select_fridge.configure(borderwidth="2")
        self.cnv_select_fridge.configure(insertbackground="black")
        self.cnv_select_fridge.configure(relief='ridge')
        self.cnv_select_fridge.configure(selectbackground="#c4c4c4")
        self.cnv_select_fridge.configure(selectforeground="black")
        self.cnv_select_fridge.configure(width=393)

        self.frm_select_fridge = tk.Frame(self.cnv_select_fridge)
        self.frm_select_fridge.place(relx=0.025, rely=0.016, relheight=0.972
                                     , relwidth=0.954)
        self.frm_select_fridge.configure(relief='groove')
        self.frm_select_fridge.configure(borderwidth="2")
        self.frm_select_fridge.configure(relief='groove')
        self.frm_select_fridge.configure(background="#d9d9d9")
        self.frm_select_fridge.configure(width=375)

        self.lbl_fridge_description = tk.Label(self.frm_select_fridge)
        self.lbl_fridge_description.place(relx=0.027, rely=0.016, height=34, width=106)
        self.lbl_fridge_description.configure(background="#d9d9d9")
        self.lbl_fridge_description.configure(disabledforeground="#a3a3a3")
        self.lbl_fridge_description.configure(font=font9)
        self.lbl_fridge_description.configure(foreground="#000000")
        self.lbl_fridge_description.configure(text='''Description:''')
        self.lbl_fridge_description.pack(side="top")

        self.lbl_add_glass_success = tk.Label(self.notebook_t1)
        self.lbl_add_glass_success.place(relx=0.027, rely=0.943, height=33, width=250)
        self.lbl_add_glass_success.configure(background="#d9d9d9")
        self.lbl_add_glass_success.configure(disabledforeground="#a3a3a3")
        self.lbl_add_glass_success.configure(font=font9)
        self.lbl_add_glass_success.configure(foreground="#AE3A3A")
        self.lbl_add_glass_success.configure(text='''Successfully Added To Glass''')
        self.lbl_add_glass_success.configure(state=tk.DISABLED)

        self.txtbx_fridge_selected = ROText(self.frm_select_fridge)
        self.txtbx_fridge_selected.place(relx=0.107, rely=0.081, relheight=0.905, relwidth=0.784)
        self.txtbx_fridge_selected.configure(background="white")
        self.txtbx_fridge_selected.configure(font="TkTextFont")
        self.txtbx_fridge_selected.configure(foreground="black")
        self.txtbx_fridge_selected.configure(highlightbackground="#d9d9d9")
        self.txtbx_fridge_selected.configure(highlightcolor="black")
        self.txtbx_fridge_selected.configure(insertbackground="black")
        self.txtbx_fridge_selected.configure(selectbackground="#c4c4c4")
        self.txtbx_fridge_selected.configure(selectforeground="black")
        self.txtbx_fridge_selected.configure(width=294)
        self.txtbx_fridge_selected.configure(wrap='word')

        self.btn_add_glass = tk.Button(self.notebook_t1)
        self.btn_add_glass.place(relx=0.836, rely=0.943, height=33, width=166)
        self.btn_add_glass.configure(activebackground="#ececec")
        self.btn_add_glass.configure(activeforeground="#000000")
        self.btn_add_glass.configure(background="#d9d9d9")
        self.btn_add_glass.configure(disabledforeground="#a3a3a3")
        self.btn_add_glass.configure(foreground="#000000")
        self.btn_add_glass.configure(highlightbackground="#d9d9d9")
        self.btn_add_glass.configure(highlightcolor="black")
        self.btn_add_glass.configure(pady="0")
        self.btn_add_glass.configure(text='''Add To Glass''')
        self.btn_add_glass.configure(width=166)
        self.btn_add_glass.bind('<Button-1>', lambda e: PyDrink_support.btn_add_glass_lclick(e, self.stv_list_fridge,
                                                                                             self.stv_list_glass,
                                                                                             self.lbl_add_glass_success)
                                )
        self.cnv_list_glass = tk.Canvas(self.notebook_t2)
        self.cnv_list_glass.place(relx=0.0, rely=0.015, relheight=0.919
                                  , relwidth=0.635)
        self.cnv_list_glass.configure(background="#d9d9d9")
        self.cnv_list_glass.configure(borderwidth="2")
        self.cnv_list_glass.configure(highlightbackground="#d9d9d9")
        self.cnv_list_glass.configure(highlightcolor="black")
        self.cnv_list_glass.configure(insertbackground="black")
        self.cnv_list_glass.configure(relief='ridge')
        self.cnv_list_glass.configure(selectbackground="#c4c4c4")
        self.cnv_list_glass.configure(selectforeground="black")
        self.cnv_list_glass.configure(width=683)

        self.frame_list_glass = tk.Frame(self.cnv_list_glass)
        self.frame_list_glass.place(relx=0.015, rely=0.016, relheight=0.972
                                    , relwidth=0.974)
        self.frame_list_glass.configure(relief='groove')
        self.frame_list_glass.configure(borderwidth="2")
        self.frame_list_glass.configure(relief='groove')
        self.frame_list_glass.configure(background="#d9d9d9")
        self.frame_list_glass.configure(highlightbackground="#d9d9d9")
        self.frame_list_glass.configure(highlightcolor="black")
        self.frame_list_glass.configure(width=665)

        self.style.configure('Treeview.Heading', font="TkDefaultFont")
        style = ttk.Style(self.style)
		#Commented out lines below left to show what attributes of Treeitem were removed
        style.layout("Treeview.Item",
                     [('Treeitem.padding', {'sticky': 'nswe', 'children':
                         [('Treeitem.indicator', {'side': 'left', 'sticky': ''}),
                          ('Treeitem.image', {'side': 'left', 'sticky': ''}),
                          # ('Treeitem.focus', {'side': 'left', 'sticky': '', 'children': [
                          ('Treeitem.text', {'side': 'left', 'sticky': ''}),
                          # ]})
                          ],
                                            })]
                     )
        self.stv_list_glass = ScrolledTreeView(self.frame_list_glass)
        self.stv_list_glass.place(relx=0.015, rely=0.016, relheight=0.486
                                  , relwidth=0.962)
        self.stv_list_glass.heading("#0", text="Drink")
        self.stv_list_glass.heading("#0", anchor="center")
        self.stv_list_glass.column("#0", width="308")
        self.stv_list_glass.column("#0", minwidth="20")
        self.stv_list_glass.column("#0", stretch="1")
        self.stv_list_glass.column("#0", anchor="w")
        self.stv_list_glass.configure(style='nodotbox.Treeview', selectmode='none')
        self.notebook_t2.bind('<Visibility>', lambda e: PyDrink_support.ntb_open_glass(e, self.stv_list_glass,
                                                                                       self.stv_list_cocktails,
                                                                                       self.txtbx_glass_selected))

        self.style.configure('Treeview.Heading', font="TkDefaultFont")
        self.stv_list_cocktails = ScrolledTreeView(self.frame_list_glass)
        self.stv_list_cocktails.place(relx=0.015, rely=0.497, relheight=0.485
                                      , relwidth=0.962)
        self.stv_list_cocktails.heading("#0", text="Cocktail")
        self.stv_list_cocktails.heading("#0", anchor="center")
        self.stv_list_cocktails.column("#0", width="308")
        self.stv_list_cocktails.column("#0", minwidth="20")
        self.stv_list_cocktails.column("#0", stretch="1")
        self.stv_list_cocktails.column("#0", anchor="center")

        self.cnv_select_glass = tk.Canvas(self.notebook_t2)
        self.cnv_select_glass.place(relx=0.632, rely=0.015, relheight=0.919
                                    , relwidth=0.365)
        self.cnv_select_glass.configure(background="#d9d9d9")
        self.cnv_select_glass.configure(borderwidth="2")
        self.cnv_select_glass.configure(highlightbackground="#d9d9d9")
        self.cnv_select_glass.configure(highlightcolor="black")
        self.cnv_select_glass.configure(insertbackground="black")
        self.cnv_select_glass.configure(relief='ridge')
        self.cnv_select_glass.configure(selectbackground="#c4c4c4")
        self.cnv_select_glass.configure(selectforeground="black")
        self.cnv_select_glass.configure(width=393)

        self.frm_select_glass = tk.Frame(self.cnv_select_glass)
        self.frm_select_glass.place(relx=0.025, rely=0.016, relheight=0.972
                                    , relwidth=0.954)
        self.frm_select_glass.configure(relief='groove')
        self.frm_select_glass.configure(borderwidth="2")
        self.frm_select_glass.configure(relief='groove')
        self.frm_select_glass.configure(background="#d9d9d9")
        self.frm_select_glass.configure(highlightbackground="#d9d9d9")
        self.frm_select_glass.configure(highlightcolor="black")
        self.frm_select_glass.configure(width=375)

        self.lbl_glass_description = tk.Label(self.frm_select_glass)
        self.lbl_glass_description.place(relx=0.027, rely=0.016, height=34, width=294)
        self.lbl_glass_description.configure(background="#d9d9d9")
        self.lbl_glass_description.configure(disabledforeground="#a3a3a3")
        self.lbl_glass_description.configure(font=font9)
        self.lbl_glass_description.configure(foreground="#000000")
        self.lbl_glass_description.configure(text='''Ingredients Needed:''')
        self.lbl_glass_description.pack(side="top")

        self.txtbx_glass_selected = ROText(self.frm_select_glass)
        self.txtbx_glass_selected.place(relx=0.107, rely=0.081, relheight=0.905, relwidth=0.784)
        self.txtbx_glass_selected.configure(background="white")
        self.txtbx_glass_selected.configure(font="TkTextFont")
        self.txtbx_glass_selected.configure(foreground="black")
        self.txtbx_glass_selected.configure(highlightbackground="#d9d9d9")
        self.txtbx_glass_selected.configure(highlightcolor="black")
        self.txtbx_glass_selected.configure(insertbackground="black")
        self.txtbx_glass_selected.configure(selectbackground="#c4c4c4")
        self.txtbx_glass_selected.configure(selectforeground="black")
        self.txtbx_glass_selected.configure(width=294)
        self.txtbx_glass_selected.configure(wrap='word')

        self.notebook.bind('<Button-1>', _button_press)
        self.notebook.bind('<ButtonRelease-1>', _button_release)
        self.notebook.bind('<Motion>', _mouse_over)


# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.
def _button_press(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        index = widget.index("@%d,%d" % (event.x, event.y))
        widget.state(['pressed'])
        widget._active = index


def _button_release(event):
    widget = event.widget
    if not widget.instate(['pressed']):
            return
    element = widget.identify(event.x, event.y)
    try:
        index = widget.index("@%d,%d" % (event.x, event.y))
    except Exception:
        pass
    if "close" in element and widget._active == index:
        widget.forget(index)
        widget.event_generate("<<NotebookTabClosed>>")

    widget.state(['!pressed'])
    widget._active = None


def _mouse_over(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        widget.state(['alternate'])
    else:
        widget.state(['!alternate'])

# The following code is added to facilitate read-only textbox
class ROText(tk.Text):
    """Configure the Text widget to be read-only."""
    # This is the list of all default command in the "Text" tag that modify the text
    commands_to_remove = ("<Control-Key-h>", "<Meta-Key-Delete>", "<Meta-Key-BackSpace>", "<Meta-Key-d>",
                          "<Meta-Key-b>", "<<Redo>>", "<<Undo>>", "<Control-Key-t>", "<Control-Key-o>",
                          "<Control-Key-k>", "<Control-Key-d>", "<Key>", "<Key-Insert>", "<<PasteSelection>>",
                          "<<Clear>>", "<<Paste>>", "<<Cut>>", "<Key-BackSpace>", "<Key-Delete>", "<Key-Return>",
                          "<Control-Key-i>", "<Key-Tab>", "<Shift-Key-Tab>")
    tagInit = False

    def init_tag(self):
        """
        Just go through all binding for the Text widget.
        If the command is allowed, recopy it in the ROText binding table.
        """
        for key in self.bind_class("Text"):
            if key not in self.commands_to_remove:
                command = self.bind_class("Text", key)
                self.bind_class("ROText", key, command)
        ROText.tagInit = True

    def __init__(self, *args, **kwords):
        tk.Text.__init__(self, *args, **kwords)
        if not ROText.tagInit:
            self.init_tag()

        # Create a new binding table list, replace the default Text binding table by the ROText one
        bind_tags = tuple(tag if tag!="Text" else "ROText" for tag in self.bindtags())
        self.bindtags(bind_tags)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    """Configure the scrollbars for a widget."""

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    """Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget."""
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    """A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed."""
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()





