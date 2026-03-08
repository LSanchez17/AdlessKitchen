import { fetchBaseQuery, type BaseQueryFn, type FetchArgs, type FetchBaseQueryError } from "@reduxjs/toolkit/query/react";

import { setToken } from '@/modules/user/user_slice';
import type { RootState } from "@/store/store";

const rawBaseQuery = fetchBaseQuery({
    baseUrl: import.meta.env.VITE_SERVER_URL || "http://localhost:8000/",
    credentials: 'include',
    prepareHeaders: (headers, { getState }) => {
        const token = (getState() as RootState).users.token;

        if (token) {
            headers.set('authorization', `Bearer ${token}`);
        }

        return headers;
    },
});

const baseQuery: BaseQueryFn<string | FetchArgs, unknown, FetchBaseQueryError> =
    async (args, api, extraOptions) => {
        const result = await rawBaseQuery(args, api, extraOptions);

        // handle redirect header as before
        const redirect = result.meta?.response?.headers?.get('X-Redirect-To');
        if (redirect) {
            window.location.href = redirect;
        }

        // update the existing token if a new one is provided in the response headers
        const newToken = result.meta?.response?.headers?.get('X-Auth-Token');
        if (newToken) {
            console.log('Received new token from server, updating local storage and state');
            localStorage.setItem('token', newToken);
            api.dispatch(setToken(newToken));
        }

        return result;
    };

export default baseQuery;