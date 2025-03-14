Algortima Pencarian memiliki 2 type yakni:
1. uninformed search adalah metode pencarian yang tidak menggunakan informasi tambahan tentang keadaan atau tujuan untuk memandu pencarian. Algoritma ini hanya menggunakan informasi yang tersedia dalam struktur data yang ada, seperti node saat ini dan hubungan antar node.
Tidak Menggunakan Heuristik, Mencari Semua Kemungkinan, dan Sederhana dan Mudah Diimplementasikan merupakan karakteristik dari uninformed search. Contoh Algoritma Uninformed Search yaitu seperti:
  1. Breadth-First Search (BFS) yaitu algoritma yang akan menjelajahi semua node pada tingkat yang sama sebelum melanjutkan ke tingkat berikutnya. Menemukan solusi terpendek 
     dalam hal jumlah langkah jika semua langkah memiliki biaya yang sama.
  2. Depth-First Search (DFS) yaitu algoritma yang akan menjelajahi sejauh mungkin di sepanjang cabang sebelum kembali. Dapat menemukan solusi yang lebih dalam tetapi tidak 
     selalu menjamin solusi terpendek.
  3. Uniform Cost Search yaitu algoritma yang akan memperluas node dengan biaya terendah terlebih dahulu. Berguna ketika langkah-langkah memiliki biaya yang berbeda.
2. informed search adalah metode pencarian yang menggunakan informasi tambahan (heuristik) untuk memandu pencarian menuju tujuan. Algoritma ini menggunakan pengetahuan tentang masalah untuk memperkirakan seberapa dekat suatu node dengan tujuan, sehingga dapat memilih jalur yang lebih efisien.
Contoh Algoritma Informed Search:
  1. Greedy Best-First Search yaitu algoritma yang akan memperluas node yang tampaknya paling dekat dengan tujuan berdasarkan heuristik, tanpa mempertimbangkan biaya dari node 
     sebelumnya.
  2. A* Graph Search ialah varian dari algoritma A* yang menyimpan informasi tentang node yang telah dikunjungi dalam struktur data, biasanya menggunakan himpunan (set) atau 
     daftar. Ini memungkinkan algoritma untuk menghindari mengunjungi node yang sama lebih dari sekali.
  3. A* Tree Search ialah varian dari algoritma A* yang tidak menyimpan informasi tentang node yang telah dikunjungi. Setiap kali algoritma memperluas node, ia menganggap 
     node tersebut sebagai node baru, bahkan jika node tersebut telah dikunjungi sebelumnya.

