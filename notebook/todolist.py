class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"'{task}' görev olarak eklendi.")

    def view_tasks(self):
        if not self.tasks:
            print("Görev listesi boş.")
            return
        for index, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{index + 1}. [{status}] {task['task']}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"{self.tasks[index]['task']} görevi tamamlandı.")
        else:
            print("Geçersiz görev numarası.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Uygulaması")
        print("1. Görev Ekle")
        print("2. Görevleri Görüntüle")
        print("3. Görevi Tamamla")
        print("4. Çıkış")
        
        choice = input("Seçiminizi yapın (1/2/3/4): ")

        if choice == "1":
            task = input("Eklenecek görevi yazın: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Tamamlamak istediğiniz görev numarasını girin: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()