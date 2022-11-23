import streamlit as st
import mysql.connector
import st_db_barang_koneksi

def hapus():
    conn = st_db_barang_koneksi.koneksi()

    st.info ('HAPUS DATA')
    kode = st.text_input ('INPUT KODE BARANG YANG MAU DI HAPUS')

    cek = st.button('DELETE DATA')
    if (cek):

        if(kode == ''):
            st.error('Silahkan Input Kode Barang yang ingin dihapus')

        else:
           sql = "SELECT * FROM barang WHERE kode_barang = '%s'" % kode
           mycursor = conn.cursor()
           mycursor.execute(sql)    
           dataku = mycursor.fetchall()

           if (len(dataku) == 0):
                st.header('KODE SALAH')

           else:
               sql = "DELETE FROM barang WHERE kode_barang = '%s'" % kode
               mycursor = conn.cursor()
               mycursor.execute(sql)
               conn.commit()
               conn.close()
               st.header ('Data telah di hapus')
               st.snow()


