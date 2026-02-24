import type { AuthenticatedResponse, LoginRequest, SignupRequest } from "../types/authentication_types";
import api from "@/api/api";

const userApi = api.injectEndpoints({
    endpoints: (builder) => ({
        login: builder.mutation<AuthenticatedResponse, LoginRequest>({
            query: (credentials) => ({
                url: 'users/login',
                method: 'POST',
                body: credentials,
            }),
        }),
        signup: builder.mutation<AuthenticatedResponse, SignupRequest>({
            query: (userInfo) => ({
                url: 'users/signup',
                method: 'POST',
                body: userInfo,
            }),
        }),
    }),
    overrideExisting: false,
})

export const { useLoginMutation, useSignupMutation } = userApi;