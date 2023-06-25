# Digital Airlines

Η Digital Airlines είναι μια διαδικτυακή εφαρμογή κατασκευασμένη με τη χρήση Flask και MongoDB. Επιτρέπει στους χρήστες να εγγράφονται, να αναζητούν πτήσεις, να κάνουν κρατήσεις και να εκτελούν άλλες σχετικές ενέργειες.

## Πώς να τρέξετε την εφαρμογή 

### Διαχειριστής

Ένας χρήστης διαχειριστής έχει τις ακόλουθες δυνατότητες:

- Δημιουργία μιας πτήσης: Ο διαχειριστής μπορεί να δημιουργήσει μια νέα πτήση παρέχοντας τα απαραίτητα στοιχεία, όπως το αεροδρόμιο αναχώρησης, το αεροδρόμιο προορισμού, την ημερομηνία πτήσης, τη διαθεσιμότητα των εισιτηρίων και το κόστος του εισιτηρίου.

- Ενημέρωση των τιμών των εισιτηρίων: Ο διαχειριστής μπορεί να ενημερώσει τις τιμές των εισιτηρίων για μια συγκεκριμένη πτήση.

- Διαγραφή μιας πτήσης: Ο διαχειριστής μπορεί να διαγράψει μια πτήση από το σύστημα. Ωστόσο, μια πτήση δεν μπορεί να διαγραφεί εάν υπάρχουν υπάρχουσες κρατήσεις που σχετίζονται με αυτήν.

- Αναζήτηση μιας πτήσης: Ο διαχειριστής μπορεί να αναζητήσει πτήσεις με βάση κριτήρια όπως το αεροδρόμιο αναχώρησης, το αεροδρόμιο προορισμού και την ημερομηνία πτήσης.

- Προβολή λεπτομερειών πτήσης: Ο διαχειριστής μπορεί να προβάλει τις λεπτομέρειες μιας συγκεκριμένης πτήσης, συμπεριλαμβανομένων των διαθέσιμων εισιτηρίων και του κόστους τους.

- Αποσύνδεση: Ο διαχειριστής μπορεί να αποσυνδεθεί από το σύστημα.

### Απλός χρήστης

Ένας απλός χρήστης έχει τις ακόλουθες δυνατότητες:

- Αναζήτηση για μια πτήση: Ο χρήστης μπορεί να αναζητήσει πτήσεις με βάση κριτήρια όπως το αεροδρόμιο αναχώρησης, το αεροδρόμιο προορισμού και την ημερομηνία πτήσης.

- Προβολή λεπτομερειών της πτήσης: Ο χρήστης μπορεί να προβάλει τις λεπτομέρειες μιας συγκεκριμένης πτήσης, συμπεριλαμβανομένων των διαθέσιμων εισιτηρίων και του κόστους τους.

- Πραγματοποίηση κράτησης: Ο χρήστης μπορεί να κάνει κράτηση για μια συγκεκριμένη πτήση παρέχοντας τις απαραίτητες πληροφορίες για τον επιβάτη.

- Εμφάνιση κρατήσεων: Ο χρήστης μπορεί να προβάλει τις υπάρχουσες κρατήσεις του.

- Εμφάνιση λεπτομερειών κράτησης: Ο χρήστης μπορεί να δει τις λεπτομέρειες μιας συγκεκριμένης κράτησης.

- Ακύρωση κράτησης: Ο χρήστης μπορεί να ακυρώσει μια συγκεκριμένη κράτηση.

- Διαγραφή του λογαριασμού: Ο χρήστης μπορεί να διαγράψει το λογαριασμό του από το σύστημα.

- Αποσύνδεση: Ο χρήστης μπορεί να αποσυνδεθεί από το σύστημα.

## Εκτέλεση του προγράμματος

Για να εκτελέσετε το πρόγραμμα Digital Airlines, ακολουθήστε τα παρακάτω βήματα:

1. Εγκαταστήστε την Python στο σύστημά σας.

2. Εγκαταστήστε τα απαιτούμενα πακέτα Python εκτελώντας την ακόλουθη εντολή: pip install -r requirements.txt

3. Βεβαιωθείτε ότι η MongoDB είναι εγκατεστημένη και εκτελείται στο σύστημά σας.

4. Ανοίξτε ένα τερματικό ή μια γραμμή εντολών και πλοηγηθείτε στον κατάλογο του έργου.

5. Εκτελέστε την ακόλουθη εντολή για να εκκινήσετε τον διακομιστή Flask:

6. Μόλις ο διακομιστής εκτελεστεί, μπορείτε να αποκτήσετε πρόσβαση στην εφαρμογή Digital Airlines στο πρόγραμμα περιήγησης ιστού σας, επισκεπτόμενοι την τοποθεσία `http://localhost:5000/home`.

7. Ακολουθήστε τις παρεχόμενες διευθύνσεις URL και τα τελικά σημεία για να αλληλεπιδράσετε με την εφαρμογή ως διαχειριστής ή ως απλός χρήστης.

Σημειώστε ότι ο αρχικός λογαριασμός διαχειριστή με τα ακόλουθα διαπιστευτήρια έχει ήδη δημιουργηθεί: python app.py

- Ηλεκτρονικό ταχυδρομείο: admin@example.com
- Κωδικός πρόσβασης: admin

Μη διστάσετε να τροποποιήσετε τον κώδικα και να προσθέσετε περισσότερη λειτουργικότητα ανάλογα με τις ανάγκες.

Καλή χρήση της εφαρμογής Digital Airlines!

# Ακολουθούν επιτυχημένα παραδείγματα αιτημάτων και οι απαντήσεις που λαμβάνουμε σε κάθε σημείο εισόδου

1. Ανοίγωντας την εφαρμογη θα βρεθούμε στην Αρχική Σελίδα απο εκεί είτε θα κάνουμε User Registration είτε θα κάνουμε Login





2. Μέτα το login
   
### Διαχειριστής

-Admin Home

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/e44231c1-d47b-410e-a7d8-f6a076794fe0)

-Create Flight

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/fd1bb2f2-5580-412e-ae73-450eba72da9f)

-Update Ticket Price

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/dc021bcd-c7d8-452a-ac5b-d4b235f28963)

-Delete Flight

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/1f4ec61a-2c3e-4fcc-99dd-03405c830eb5)

3. Μετά το User Registration

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/cc9de386-c76f-45be-a3c8-7093733bd68c)


### Απλός χρήστης

-Simple User Home

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/51650538-9902-4f79-8cec-0c58055759c0)

- Make Reservation

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/db6ca3e8-1365-4744-9ce3-24a41b800830)

- Display Reservations

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/9a2b5bb1-893c-43fe-a37f-cbd3781cfb60)

-  Display Reservation Details
  
![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/b6bceb3a-eafe-488a-abd4-d93e004ab7f1)

-  Cancel Reservation

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/5daab495-02a1-429f-b234-8aa6ce27aefb)

-  Delete Account

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/6d1ba60a-c860-4567-a909-4b80debbc300)


4. Κοινές διαδικασίες και για τους 2 χρήστες

-Search Flight

all

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/389b50ab-5455-4d50-99e4-0c9ed0659165)

by_date

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/8c144151-99d8-456f-bc5e-cee5199cd5c2)

-Flight Details

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/753c5dd4-3024-40ef-ab46-bafc6d6be7e6)

-Logout

![image](https://github.com/nenikolaidis/YpoxreotikiErgasia23_e20113_Nikolaidis_Nearchos/assets/129533209/b09e41b0-8fb0-4728-9e8d-43df57fa9dd8)


  
