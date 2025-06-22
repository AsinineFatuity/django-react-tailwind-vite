FEEDBACK_TOAST_REDUCER_CONTENT = """
import { FEEDBACK_TOAST } from "../actions/types";
import { FeedBackToastType } from "./src/helpers/interfaces";

const initialState: FeedBackToastType = {
  type: "default",
  message: "",
};

function setFeedbackToast(
  type: FeedBackToastType["type"],
  message: FeedBackToastType["message"],
) {
  return {
    type,
    message,
  };
}

export const feedbackToastReducer = (state = initialState, action: any) => {
  if (!action.errors) {
    if (action.type === FEEDBACK_TOAST.showCustomFeedbackToast) {
      return setFeedbackToast(action.payload.type, action.payload.message);
    } else {
      return state;
    }
  } else {
    if (
      Array.isArray(action.errors) &&
      action.errors.length > 0 &&
      "message" in action.errors[0]
    ) {
      return setFeedbackToast("error", action.errors[0]["message"]);
    } else if (action.errors && typeof action.errors === "string") {
      return setFeedbackToast("error", action.errors);
    }
    return setFeedbackToast("error", "Could not complete action");
  }
};

"""

LOADING_INDICATOR_REDUCER_CONTENT = """
import { LOADING_INDICATOR } from "../actions/types";

const determineLoadingIndicatorState = (
  currentState: number,
  payload: boolean,
) => {
  if (currentState >= 0) {
    if (payload) {
      currentState += 1;
    } else if (currentState - 1 >= 0) {
      currentState -= 1;
    }
  }
  return currentState;
};

export const loadingIndicatorReducer = (state = 0, action: any) => {
  let currentState = state;
  if (action.type === LOADING_INDICATOR.showLoadingIndicator) {
    return determineLoadingIndicatorState(currentState, action.payload);
  } else if (action?.payload?.isComplete) {
    return determineLoadingIndicatorState(currentState, false);
  }
  return currentState;
};
"""

REDUCER_INDEX_CONTENT = """
import { loadingIndicatorReducer } from "./loadingIndicator";
import { feedbackToastReducer } from "./feedbackToast";

export const sliceReducers = {
  isLoading: loadingIndicatorReducer,
  feedbackToast: feedbackToastReducer,
};

export default sliceReducers;
"""
