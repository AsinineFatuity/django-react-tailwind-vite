INTERFACES_FILE_CONTENT = """
import { Action } from "redux";

export interface MiddlewareActionType extends Action {
  type: string;
  payload: {
    isComplete: boolean;
    feedbackToast: FeedBackToastType;
    appendData: boolean;
    [key: string]: any;
  };
}

export interface FeedBackToastType {
  type: "info" | "success" | "warning" | "error" | "default";
  message: string;
}
"""

UTILS_FILE_CONTENT = """
import { MiddlewareActionType } from "./interfaces";
export const createMiddlewareAction = (
  type: string,
  payload: object = {},
  appendData: boolean = false,
): MiddlewareActionType => {
  return {
    type,
    payload: {
      ...payload,
      isComplete: false,
      appendData: appendData,
      feedbackToast: {type: "default", message: ""},
    },
  };
};

export const APP_URLS = {
  home: "/",
};
"""
