import type { Response } from "@/api/types";
import type { LoginRequest, SignupRequest } from "../types/authentication_types";
import api from "@/api/api";
import type { User } from "@/modules/user/types";

const userApi = api.injectEndpoints({
    endpoints: (builder) => ({
        login: builder.mutation<Response<User>, LoginRequest>({
            query: (credentials) => ({
                url: 'users/login',
                method: 'POST',
                body: credentials,
            }),
        }),
        signup: builder.mutation<Response<User>, SignupRequest>({
            query: (userInfo) => ({
                url: 'users/signup',
                method: 'POST',
                body: userInfo,
            }),
        }),
        logout: builder.mutation<void, void>({
            query: () => ({
                url: 'users/logout',
                method: 'POST',
            }),
        }),
    }),
    overrideExisting: false,
})

export const { useLoginMutation, useSignupMutation, useLogoutMutation } = userApi;
export { userApi };