import type { PayloadAction } from '@reduxjs/toolkit';
import { createSlice } from '@reduxjs/toolkit';

import type { RootState } from '@/store/store';
import { userApi } from '@/api/endpoints/user/user_api';
import type { Response } from '@/api/types';
import type { User } from './types';


const initialState: User = {
    firstName: undefined,
    lastName: undefined,
    email: undefined,
    id: undefined,
    token: localStorage.getItem('token') ?? undefined,
};

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        logout(state) {
            state.firstName = undefined;
            state.lastName = undefined;
            state.email = undefined;
            state.id = undefined;
            state.token = undefined;
            localStorage.removeItem('token');
        },
        setToken(state, action: PayloadAction<string | null>) {
            state.token = action.payload ?? undefined;
        },
    },
    extraReducers(builder) {
        builder.addMatcher(
            userApi.endpoints.login.matchFulfilled,
            (state, action: PayloadAction<Response<User>>) => {
                const result = action.payload.results[0];
                state.firstName = result.firstName ?? undefined;
                state.lastName = result.lastName ?? undefined;
                state.email = result.email ?? undefined;
                state.id = result.id ?? undefined;
            }
        ),
            builder.addMatcher(
                userApi.endpoints.signup.matchFulfilled,
                (state, action: PayloadAction<Response<User>>) => {
                    const result = action.payload.results[0];
                    state.firstName = result.firstName ?? undefined;
                    state.lastName = result.lastName ?? undefined;
                    state.email = result.email ?? undefined;
                    state.id = result.id ?? undefined;
                }
            )
    },
});

export const { logout, setToken } = userSlice.actions;

export const selectCurrentUser = (state: RootState) => state.users;
export const selectIsUserLoggedIn = (state: RootState) => !!state.users.token;

export default userSlice.reducer;
