import http from "./http-common";

class TodoApi {
    getAll() {
        return http.get("/tasks/")
    }
    getDetails(id) {
        return http.get(`/task-detail/${id}`)
    }
    create(data) {
        return http.post("/task-create/", data);
    }

    update(id, data) {
        return http.put(`/task-update/${id}`, data);
    }

    delete(id) {
        return http.delete(`/task-delete/${id}`);
    }
}
export default new TodoApi();