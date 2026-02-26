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
        },
        setUser(state, action: PayloadAction<User | null>) {
            const user = action.payload;
            state.firstName = user?.firstName ?? undefined;
            state.lastName = user?.lastName ?? undefined;
            state.email = user?.email ?? undefined;
            state.id = user?.id ?? undefined;
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
        );
    },
});

export const { logout, setUser } = userSlice.actions;

export const selectCurrentUser = (state: RootState) => state.users.id;
export const selectIsUserLoggedIn = (state: RootState) => !!state.users.token;

export default userSlice.reducer;
