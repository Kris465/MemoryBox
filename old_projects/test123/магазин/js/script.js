document.querySelectorAll('.quantity-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const index = this.dataset.index;
        const input = document.getElementById(`quantity-${index}`);
        let value = parseInt(input.value);
        
        if (this.classList.contains('minus')) {
            if (value > 1) value--;
        } else if (this.classList.contains('plus')) {
            value++;
        }
        input.value = value;
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('fieldsContainer');
    const addBtn = document.getElementById('addFieldBtn');
    
    addBtn.addEventListener('click', function() {
        const newRow = document.createElement('div');
        newRow.className = 'field-row';
        newRow.innerHTML = `
            <input type="text" name="field_name[]" placeholder="Название поля" class="form-control field-name">
            <select name="field_type[]" class="form-control field-type">
                <option value="text">Текст</option>
                <option value="number">Число</option>
                <option value="textarea">Текст (многострочный)</option>
            </select>
            <button type="button" class="btn btn-remove-field">×</button>
        `;
        container.appendChild(newRow);
        updateRemoveButtons();
            });
    container.addEventListener('input', function(e) {
        if (e.target.classList.contains('field-name')) {
            const rows = container.querySelectorAll('.field-row');
            const lastRow = rows[rows.length - 1];
            const input = lastRow.querySelector('.field-name');
            
            if (input.value.trim() !== '' && input === e.target) {
                addBtn.click();
            }
        }
    });
    function updateRemoveButtons() {
        document.querySelectorAll('.btn-remove-field').forEach(btn => {
            btn.addEventListener('click', function() {
                if (container.querySelectorAll('.field-row').length > 1) {
                    this.parentElement.remove();
                }
            });
        });
    }
    updateRemoveButtons();
});

function showCategoryFields(select) {
    const container = document.getElementById('categoryFieldsContainer');
    container.innerHTML = '';
    
    const categoryName = select.value;
    const categories = <?= json_encode(array_map(function($c) { 
        return ['name' => $c->name, 'fields' => $c->fields ?? []]; 
    }, $_SESSION['categories'] ?? [])) ?>;
    
    const category = categories.find(c => c.name === categoryName);
    if (category && category.fields.length > 0) {
        category.fields.forEach((field, index) => {
            const div = document.createElement('div');
            div.className = 'form-group';
            
            let input;
            if (field.type === 'textarea') {
                input = `<textarea name="category_fields[${field.name}]" class="form-control" ${index === 0 ? 'required' : ''}></textarea>`;
            } else {
                input = `<input type="${field.type}" name="category_fields[${field.name}]" class="form-control" ${index === 0 ? 'required' : ''}>`;
            }
            
            div.innerHTML = `
                <label>${field.name}</label>
                ${input}
            `;
            container.appendChild(div);
        });
    }
}