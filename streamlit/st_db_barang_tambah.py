import streamlit as st
import st_db_barang_koneksi

def tambah():
    st.info('TAMBAH DATA BARANG')
    kode = st.text_input ('KODE BARANG')
    nama = st.text_input ('NAMA BARANG')
    satuan = st.selectbox ('SATUAN',['PCS','DUS','RIM','LUSIN'])
    stok = st.number_input ('STOK BARANG')

    # tombol
    cek = st.button ('SAVE')
    if (cek):
        if (kode == ''):
            st.error ('KODE BARANG BELUM DI INPUT')
        
        else:
            conn = st_db_barang_koneksi.koneksi()

        sql = "select * from barang where kode_barang = '%s'" % kode
        mycursor = conn.cursor()
        mycursor.execute(sql)
        dataku = mycursor.fetchall()

        ada = (len(dataku))
        if (ada > 0):
            st.error ('KODE SUDAH ADA, SAVE DI BATALKAN')

        else:
            sql = "insert into barang (kode_barang,nama_barang,satuan,stok) \
                value (%s,%s,%s,%s)"

            dt = (kode,nama,satuan,stok)

            mycursor = conn.cursor()
            mycursor.execute(sql, dt)
            conn.commit()
            conn.close()

            st.header ('Data telah disimpan')
            st.balloons()