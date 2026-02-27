import api from "@/api/api";
import { combineReducers } from "@reduxjs/toolkit";
import userReducer from '@/modules/user/user_slice'


const applicationReducer = combineReducers({
    [api.reducerPath]: api.reducer,
    users: userReducer
    // Add other reducers here
})

export default applicationReducer;