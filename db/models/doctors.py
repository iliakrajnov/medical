def config(db):
    class doctors(db.Model):

        def __init__(self, surname, name, middle_name, cab, login, timetable, speciality):
            self.surname = surname
            self.name = name
            self.middle_name = middle_name
            self.cab = cab
            self.login = login
            self.timetable = timetable
            self.speciality
        surname = db.Column(db.String(100))
        name = db.Column(db.String(100))
        middle_name = db.Column(db.String(100))
        cab = db.Column(db.Integer)
        login = db.Column(db.String(100), primary_key=True)
        timetable = db.Column(db.String(10000))
        speciality = db.Column(db.String(10000))
    return doctors
