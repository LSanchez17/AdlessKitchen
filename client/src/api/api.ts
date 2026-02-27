import { createApi } from "@reduxjs/toolkit/query/react";
import baseQuery from "./base_query";

const api = createApi({
    reducerPath: 'api',
    baseQuery,
    endpoints: () => ({}),
});

export default api;