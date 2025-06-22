ACTION_TYPES_CONTENT = """
export const LOADING_INDICATOR = {
  showLoadingIndicator: "loadingIndicator/showLoadingIndicator",
};

export const FEEDBACK_TOAST = {
  showFeedbackToast: "feedbackToast/showFeedBackToast",
  showCustomFeedbackToast: "feedbackToast/showCustomFeedBackToast",
};
"""

FEEDBACK_TOAST_ACTION_CONTENT = """
import { FEEDBACK_TOAST } from "./types";
import { FeedBackToastType } from "../../helpers/interfaces";

export const showCustomFeedbackToast = (
  message: FeedBackToastType["message"],
  type: FeedBackToastType["type"],
) => {
  return {
    type: FEEDBACK_TOAST.showCustomFeedbackToast,
    payload: { message, type },
  };
};
"""

LOADING_INDICATOR_ACTION_CONTENT = """
import { LOADING_INDICATOR } from "./types";

export const showLoadingIndicator = (showIndicator: boolean) => {
  return {
    type: LOADING_INDICATOR.showLoadingIndicator,
    payload: showIndicator,
  };
};
"""

ACTIONS_INDEX_TS_CONTENT = """
import { showLoadingIndicator } from "./loadingIndicator";
import { showCustomFeedbackToast } from "./feedbackToast";

export { showLoadingIndicator, showCustomFeedbackToast };
"""
