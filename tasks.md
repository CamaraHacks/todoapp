# 🎯 **Tech Lead Tasks - Projeto Quick Tasks**

## **📋 SPRINT 1: Foundation (Dia 1 - 25 min)**

### **✅ TASK 1.1: Setup do App (5 min)**
```bash
# Terminal
python manage.py startapp tasks
```

**Checklist:**
Está ótimo 
 
Acho que podemos tirar o serviço e deixar produtos da Microsoft para ficar menos técnico talvez 
 
Ou nuvem da Microsoft 
 - [ x] App `tasks` criado
- [ x] Adicionado em `INSTALLED_APPS`
- [ x] Pasta `templates/tasks` criada

### **✅ TASK 1.2: Model Básico (8 min)**
```python
# tasks/models.py
class Task(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
```

**Checklist:**
- [ x] Model Task criado
- [ x] Migrations criadas (`makemigrations`)
- [ x] Migrations aplicadas (`migrate`)

### **✅ TASK 1.3: Admin Básico (7 min)**
```python
# tasks/admin.py
admin.site.register(Task)
```

**Checklist:**
- [x ] Task registrado no admin
- [ x] Conseguir adicionar tarefas via admin
- [ x] Ver tarefas na lista do admin

### **✅ TASK 1.4: Teste Final (5 min)**
**Checklist:**
- [ x] Servidor roda (`runserver`)
- [ x] Acesso `http://localhost:8000/admin`
- [ x] Criar 2-3 tarefas teste via admin

---

## **📋 SPRINT 2: Visualização (Dia 2 - 25 min)**

### **✅ TASK 2.1: View de Listagem (8 min)**
```python
# tasks/views.py
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
```

### **✅ TASK 2.2: Template Básico (7 min)**
```html
<!-- tasks/task_list.html -->
<h1>Minhas Tarefas</h1>
{% for task in task_list %}
    <p>{{ task.title }}</p>
{% endfor %}
```

### **✅ TASK 2.3: URLs (5 min)**
```python
# tasks/urls.py e projeto/urls.py
path('tasks/', TaskListView.as_view(), name='task_list')
```

### **✅ TASK 2.4: Teste (5 min)**
**Checklist:**
- [x ] Acesso `http://localhost:8000/tasks/`
- [ x] Vejo tarefas criadas via admin
- [ x] Lista funciona sem errors

---

## **📋 SPRINT 3: Criação (Dia 3 - 25 min)**

### **✅ TASK 3.1: View de Criação (8 min)**
```python
# tasks/views.py
class TaskCreateView(CreateView):
    model = Task
    fields = ['title']
    success_url = reverse_lazy('task_list')
```

### **✅ TASK 3.2: Template de Form (7 min)**
```html
<!-- tasks/task_form.html -->
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Criar</button>
</form>
```

### **✅ TASK 3.3: URL e Link (5 min)**
```python
# tasks/urls.py
path('new/', TaskCreateView.as_view(), name='task_create')
```
	
```html
<!-- Adicionar em task_list.html -->
<a href="{% url 'task_create' %}">Nova Tarefa</a>
```

### **✅ TASK 3.4: Teste (5 min)**
**Checklist:**
- [x] Link "Nova Tarefa" funciona
- [x] Formulário aparece
- [x] Consigo criar tarefa e redireciona para lista

---

## **📋 SPRINT 4: Melhorias (Dia 4 - 25 min)**

### **✅ TASK 4.1: Campo Description (8 min)**
```python
# tasks/models.py - adicionar
description = models.TextField(blank=True)

# tasks/views.py - atualizar
fields = ['title', 'description']
```

### **✅ TASK 4.2: Marcar como Feito (7 min)**
```python
# tasks/views.py - adicionar
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'done']
    success_url = reverse_lazy('task_list')
```

### **✅ TASK 4.3: URLs e Links (5 min)**
```python
# tasks/urls.py
path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update')
```

### **✅ TASK 4.4: Teste (5 min)**
**Checklist:**
- [x] Description aparece nos forms
- [X] Checkbox "done" funciona
- [X] Edição mantém dados

---

## **📋 SPRINT 5: Polimento (Dia 5 - 25 min)**

### **✅ TASK 5.1: Ordenação (5 min)**
```python
# tasks/models.py
class Meta:
    ordering = ['-created_date']
```

### **✅ TASK 5.2: Filtro Não Concluídas (8 min)**
```python
# tasks/views.py
def get_queryset(self):
    return Task.objects.filter(done=False)
```

### **✅ TASK 5.3: CSS Básico (7 min)**
```html
<!-- Adicionar em task_list.html -->
<style>
.done { text-decoration: line-through; }
</style>
```

### **✅ TASK 5.4: Teste Final (5 min)**
**Checklist:**
- [ ] Tarefas ordenadas por data
- [ ] Só mostra não concluídas
- [ ] Estilo visual básico funciona

---

## **🎯 CRITÉRIOS DE SUCESSO**

**✅ PROJETO MÍNIMO VIÁVEL:**
- [ ] Criar tarefas via formulário
- [ ] Listar tarefas não concluídas  
- [ ] Marcar como feito
- [ ] Interface funcional

**🚀 BÔNUS (se sobrar tempo):**
- [ ] Deletar tarefas
- [ ] Pesquisa por título
- [ ] Data de vencimento

---

## **💡 DICAS DO TECH LEAD**

1. **Foque em UMA sprint por dia** - não tente adiantar
2. **Teste CADA task** antes de seguir para próxima
3. **Commite no Git** ao final de cada sprint
4. **Comemore cada progresso** - você está construindo músculo de desenvolvimento!

**Precisa de ajuda em alguma task específica? Estou aqui!** 🚀

---

*Arquivo salvo como `projeto_quick_tasks.md` - Use como seu guia diário!*
