import type { FetchArgs } from "@reduxjs/toolkit/query/react";

const prepareHeaders = (extraOptions?: FetchArgs) => {
    const token = localStorage.getItem('token');

    if (token) {
        const existingHeaders = extraOptions?.headers ?? {};
        return {
            ...(extraOptions || {}),
            headers: {
                ...existingHeaders,
                Authorization: `Bearer ${token}`,
            },
        } as FetchArgs;
    }

    return extraOptions;
}

export default prepareHeaders;