#File CRUD LIHAT DATA BARANG
import streamlit as st
import st_db_barang_koneksi		#koneksi ke db server

import { Grid } from 'ag-grid-community';

import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';

def lihat():
	#buka koneksi db
	conn = st_db_barang_koneksi.koneksi()

	#ambil data
	mycursor = conn.cursor()
	mycursor.execute ('select * from barang order by kode_barang')

    # ambil data nya
	dataku = mycursor.fetchall()
	nomer = 0	#buat nomer urut
	tstok = 0	#total stok akhir laporan

    # looping baca data
	st.warning ('LAPORAN DATA BARANG')
	st.write ('No - Kode - Nama Barang - Satuan - Stok')
	st.write ('=======================================')
	for dt in dataku:
		nomer = nomer + 1
		xkd = dt[0]
		xnm = dt[1]
		xsatuan = dt[2]
		xstok = dt[3]
		
        # hitung total stok
		tstok = tstok + xstok		

		st.write (f'({nomer}). {xkd}, {xnm}, {xsatuan},{xstok}')
		
	
	var gridOptions = {
	columnDefs: [
		{ headerName: 'No', field: 'nomer' },
		{ headerName: 'Kode', field: 'xkd' },
		{ headerName: 'Nama Barang', field: 'xnm' }
		{ headerName: 'Satuan', field: 'xsatuan' }
		{ headerName: 'Stok', field: 'xstok' }
	],
	rowData: [
		{ nomer: '{nomer}', xkd: '{xkd}', xnm: '{xnm}', xsatuan: '{xsatuan}', xstok: '{xstok}', }
	]
};

	var eGridDiv = document.querySelector('#myGrid');
	new Grid(eGridDiv, this.gridOptions);

	st.success (f'Total Stok = {tstok}')
	st.balloons()
	
	conn.close() #tutup koneksi