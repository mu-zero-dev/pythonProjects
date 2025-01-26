class Visitor:
    def __init__(self, name, contact, purpose):
        self.name = name
        self.contact = contact
        self.purpose = purpose

    def __str__(self):
        return f"Visitor(name={self.name}, contact={self.contact}, purpose={self.purpose})"

class VisitorManagementSystem:
    def __init__(self):
        self.visitors = []

    def add_visitor(self, visitor):
        self.visitors.append(visitor)
        print(f"Visitor {visitor.name} added.")

    def remove_visitor(self, name):
        for visitor in self.visitors:
            if visitor.name == name:
                self.visitors.remove(visitor)
                print(f"Visitor {name} removed.")
                return
        print(f"Visitor {name} not found.")

    def list_visitors(self):
        if not self.visitors:
            print("No visitors currently.")
        for visitor in self.visitors:
            print(visitor)

# Example Usage
vms = VisitorManagementSystem()
vms.add_visitor(Visitor("John Doe", "555-1234", "Business Meeting"))
vms.add_visitor(Visitor("Jane Smith", "555-5678", "Interview"))
vms.list_visitors()
vms.remove_visitor("John Doe")
vms.list_visitors()

