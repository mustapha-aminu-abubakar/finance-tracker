from application import app, db
from flask import render_template, flash, redirect, request, url_for
from .forms import IncomeForm, ExpenseForm, UpdateIncomeForm, UpdateExpenseForm
from datetime import datetime as dt, timedelta as td
from bson import ObjectId

@app.route("/")
def show_finances(per_page = 5):
    page = request.args.get('page', 1, type=int)
    type_ = request.args.get('type_')
    start = (page - 1) * per_page #first item in the page
    end = start + per_page #last item in the page
    
    if type_ == "income":
        items = list(db.finances.find({"type": "income"}).sort({"date": -1}))
        total_pages = (db.finances.count_documents({"type": "income"}) + per_page -1) // per_page
    elif type_ == "expense":
        items = list(db.finances.find({"type": "expense"}).sort({"date": -1}))
        total_pages = (db.finances.count_documents({"type": "expense"}) + per_page -1) // per_page
    else:
        items = list(db.finances.find().sort({"date": -1}))
        total_pages = (db.finances.count_documents({}) + per_page -1) // per_page
        
    
    items_on_page = items[start:end]
    for item in items_on_page:
            item["_id"] = str(item["_id"])
            item["date"] = item["date"].strftime("%d %b %Y, %I:%M %p")
            item["amount"] = round(item["amount"], 2)
    return render_template("show_finances.html", items_on_page=items_on_page, page=page, total_pages=total_pages, type_=type_)
    

@app.route("/add_income", methods=["POST", "GET"])
def add_income():
    if request.method == "POST":
        form = IncomeForm(request.form)
        form_amount = form.amount.data
        form_description = form.description.data
        form_source = form.source.data
        form_date = form.date_.data
        
        db.finances.insert_one({
            "amount": form_amount,
            "description": form_description,
            "date": form_date,
            "source": form_source,
            "type": "income",
        })
        
        return redirect("/")
    
    form = IncomeForm()
    return render_template("add_income.html", form=form)
  
  
@app.route("/add_expense", methods=["POST", "GET"])  
def add_expense():
    if request.method == "POST":
        form = ExpenseForm(request.form)
        form_amount = form.amount.data
        form_description = form.description.data
        form_beneficiary = form.beneficiary.data
        form_date = form.date_.data

        db.finances.insert_one({
            "amount": form_amount,
            "description": form_description,
            "date": form_date,
            "beneficiary": form_beneficiary,
            "type": "expense",
        })
        
        return redirect("/")
    
    form = ExpenseForm()
    return render_template("add_expense.html", form=form)


@app.route("/update/<id>", methods=["POST", "GET"])
def update_item(id):
    item = db.finances.find_one({"_id": ObjectId(id)})    
    if request.method == "POST":
        if item["type"] == "income":
            form = UpdateIncomeForm(request.form)
            form_amount = form.amount.data
            form_description = form.description.data
            form_source = form.source.data
            form_date = form.date_.data
            
            db.finances.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
                "amount": form_amount if form_amount else item["amount"],
                "description": form_description if form_description else item["description"],
                "source": form_source if form_source else item["source"],
                "date": str(form_date) if form_date else item["date"]
            }})      
            
            return redirect("/")
        
        elif item["type"] == "expense":
            form = UpdateExpenseForm(request.form)
            form_amount = form.amount.data
            form_description = form.description.data
            form_beneficiary = form.beneficiary.data  
            form_date = form.date_.data
            
            db.finances.find_one_and_update({"_id": ObjectId(id)},  {"$set": {
                "amount": form_amount if form_amount else item["amount"],
                "description": form_description if form_description else item["description"],
                "beneficiary": form_beneficiary if form_beneficiary else item["beneficiary"],
                "date": str(form_date) if form_date else item["date"]
                }})      
            
            return redirect("/")
        
    else:
        form = UpdateIncomeForm() if item["type"] == "income" else UpdateExpenseForm()
        placeholders= {
            "amount" : item.get("amount"),
            "description" : item.get("description"),
            "source" : item.get("source", None),
            "date" : item.get("date"),
            "beneficiary" : item.get("beneficiary", None),
        }
        
            
            
    return render_template("update_income.html" if item["type"] == "income" else "update_expense.html", form=form, 
                           placeholders=placeholders)
    

@app.route("/delete/<id>")
def delete_item(id):
    db.finances.find_one_and_delete({"_id": ObjectId(id)})
    return redirect("/")




