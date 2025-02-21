import typer
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime, timezone
import calendar

app = typer.Typer()
Base = declarative_base()

# Define a BudgetItem model
class BudgetItem(Base):
    __tablename__ = "budget_items"
    id = Column(Integer, primary_key=True)
    item = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    date_added = Column(DateTime, default=lambda: datetime.now(timezone.utc))

# Setup SQLite database
engine = create_engine("sqlite:///budget.db", echo=False)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

@app.command()
def add(item: str, price: float):
    """
    Add a new budget item.
    """
    session = SessionLocal()
    new_item = BudgetItem(item=item, price=price, date_added=datetime.now(timezone.utc))
    session.add(new_item)
    session.commit()
    session.close()
    typer.echo(f"Added item: {item} with price Rs. {price}")

@app.command()
def summary(month: str, year: int):
    """
    Calculate monthly budget summary for a given month and year.
    Month should be provided as a three-letter abbreviation (e.g., Feb).
    """
    session = SessionLocal()

    # Convert month abbreviation to month number
    try:
        month_number = list(calendar.month_abbr).index(month.capitalize())
    except ValueError:
        typer.echo("Invalid month abbreviation. Use three letters, e.g., Feb")
        session.close()
        raise typer.Exit()

    # Calculate the start date and the start of the next month (timezone naive)
    # To compare consistently, convert these to UTC timezone-aware datetimes
    start_date = datetime(year, month_number, 1, tzinfo=timezone.utc)
    if month_number == 12:
        end_date = datetime(year + 1, 1, 1, tzinfo=timezone.utc)
    else:
        end_date = datetime(year, month_number + 1, 1, tzinfo=timezone.utc)

    # Filter items added in the specified month and year.
    items = session.query(BudgetItem).filter(
        BudgetItem.date_added >= start_date,
        BudgetItem.date_added < end_date
    ).all()
    session.close()

    total = sum(item.price for item in items)
    typer.echo(f"{month}-{year} -> Output : Rs. {total:.2f}")

if __name__ == "__main__":
    app()
