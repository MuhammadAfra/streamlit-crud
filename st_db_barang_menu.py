import streamlit as st
import st_db_barang_tambah
import st_db_barang_lihat
import st_db_barang_edit
import st_db_barang_hapus
import st_db_barang_pdf

#kumpulan function
# ---------- halaman home ----------
def menu_home():
	st.header ('PROGRAM CRUD DATA BARANG')
	st.subheader ('dengan Pyhton Framework Streamlit')

# ---------- FILE CRUD ----------
def menu_input():
    st_db_barang_tambah.tambah()

def menu_edit():
    st_db_barang_edit.edit()

def menu_hapus():
    st_db_barang_hapus.hapus()

def menu_lihat():
    st_db_barang_lihat.lihat()

def menu_print_pdf():
    st_db_barang_pdf.print_pdf()

# ---------- halaman programmer ----------
def menu_programmer():
	st.info('Programmer')
	st.write ('Muhammad Afra')
	st.write ('Email = muhammadafra45@gmail.com')
		
# ---------- utama, menu side bar ----------
def menu():
	with st.sidebar:
		pilih = st.selectbox ('Menu Barang',\
		['Home','Programmer','Input Data',\
		'Edit Data', 'Hapus Data',\
		'Lihat Data','Print PDF'])
	
	if (pilih == 'Home'):
		menu_home()
	elif (pilih == 'Programmer'):
		menu_programmer()
	elif (pilih == 'Input Data'):
		menu_input()
	elif (pilih == 'Edit Data'):
		menu_edit()
	elif (pilih == 'Hapus Data'):
		menu_hapus()
	elif (pilih == 'Lihat Data'):
		menu_lihat()
	else:
		menu_print_pdf()
	
def main():
	menu()
	
if __name__ == '__main__':
	main()