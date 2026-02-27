import { fetchBaseQuery, type BaseQueryFn, type FetchArgs, type FetchBaseQueryError } from "@reduxjs/toolkit/query/react";

import { setToken } from '@/modules/user/user_slice';
import prepareHeaders from "./utils/prepare_headers";

const rawBaseQuery = fetchBaseQuery({
    baseUrl: import.meta.env.VITE_SERVER_URL || "http://localhost:8000/",
    credentials: 'include',
});

const baseQuery: BaseQueryFn<string | FetchArgs, unknown, FetchBaseQueryError> =
    async (args, api, extraOptions) => {
        const modifiedExtraOptions = prepareHeaders(extraOptions)
        const result = await rawBaseQuery(args, api, modifiedExtraOptions);

        // handle redirect header as before
        const redirect = result.meta?.response?.headers?.get('X-Redirect-To');
        if (redirect) {
            window.location.href = redirect;
        }

        // update the existing token if a new one is provided in the response headers
        const newToken = result.meta?.response?.headers?.get('X-Auth-Token');
        console.log('newtoken', newToken);
        if (newToken) {
            console.log('Received new token from server, updating local storage and state');
            localStorage.setItem('token', newToken);
            api.dispatch(setToken(newToken));
        }

        return result;
    };

export default baseQuery;