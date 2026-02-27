import api from "@/api/api";

const configureMiddleWare = (getDefaultMiddleware: any) =>
    getDefaultMiddleware({ serializableCheck: true }).concat(api.middleware);

export default configureMiddleWare;