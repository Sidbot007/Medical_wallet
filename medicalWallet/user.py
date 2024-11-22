class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.permissions = []

    def grant_permission(self, record_id):
        if record_id not in self.permissions:
            self.permissions.append(record_id)

    def revoke_permission(self, record_id):
        if record_id in self.permissions:
            self.permissions.remove(record_id)
