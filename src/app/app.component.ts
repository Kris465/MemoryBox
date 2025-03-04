import { Component } from "@angular/core";
import { FormsModule }   from "@angular/forms";
      
class Item{
    purchase: string;
    done: boolean;
    price: number;
      
    constructor(purchase: string, price: number) {
   
        this.purchase = purchase;
        this.price = price;
        this.done = false;
    }
}
  
@Component({
    selector: "purchase-app",
    standalone: true,
    imports: [FormsModule],
    template: `
        <h1> Список покупок </h1>
        <div>
            <p>
                <label>Товар</label><br>
                <input [(ngModel)]="text" />
            </p>
            <p>
                <label>Цена</label><br>
                <input type="number" [(ngModel)]="price" />
            </p>
            <button (click)="addItem(text, price)">Добавить</button>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Предмет</th>
                    <th>Цена</th>
                    <th>Куплено</th>
                </tr>
            </thead>
            <tbody>
            @for (item of items; track item.purchase) {
                <tr>
                    <td>{{item.purchase}}</td>
                    <td>{{item.price}}</td>
                    <td><input type="checkbox" [(ngModel)]="item.done" /></td>
                </tr>
            }
            </tbody>
        </table>`
})
export class AppComponent { 
    text: string = "";
    price: number = 0;
      
    items: Item[] = 
    [
        { purchase: "Хлеб", done: false, price: 15.9 },
        { purchase: "Масло", done: false, price: 60 },
        { purchase: "Картофель", done: true, price: 22.6 },
        { purchase: "Сыр", done: false, price:310 }
    ];
    addItem(text: string, price: number): void {
          
        if(text==null || text.trim()=="" || price==null)
            return;
        this.items.push(new Item(text, price));
    }
}