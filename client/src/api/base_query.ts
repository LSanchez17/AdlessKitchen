import { fetchBaseQuery, type BaseQueryFn, type FetchArgs, type FetchBaseQueryError } from "@reduxjs/toolkit/query/react";

const rawBaseQuery = fetchBaseQuery({
    baseUrl: import.meta.env.VITE_SERVER_URL || "http://localhost:8000/",
    credentials: 'include',
});

const baseQuery: BaseQueryFn<string | FetchArgs, unknown, FetchBaseQueryError> =
    async (args, api, extraOptions) => {
        const result = await rawBaseQuery(args, api, extraOptions);

        const redirect = result.meta?.response?.headers?.get('X-Redirect-To');
        if (redirect) {
            window.location.href = redirect;
        }

        return result;
    };

export default baseQuery;