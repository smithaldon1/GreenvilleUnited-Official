from app import db

goal = Main(name="d_goal", value="50000")
totals = Main(name="d_totals", value="500")

db.session.add([totals, goal])
db.session.commit()