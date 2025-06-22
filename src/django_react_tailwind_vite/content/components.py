FEEDBACK_TOAST_TSX_CONTENT = """
import React, { useEffect } from "react";
import { toast } from "react-toastify";
import { useAppSelector } from "../hooks";

export const FeedbackToast = () => {
  const feedbackToast = useAppSelector((state) => state.feedbackToast);
  useEffect(() => {
    if (feedbackToast.message) {
      toast(feedbackToast.message, {
        type: feedbackToast.type,
        autoClose: 4000,
        hideProgressBar: true,
        theme: "colored",
        position: "bottom-right",
      });
    }
  }, [feedbackToast]);

  return null;
};
"""

LOADING_INDICATOR_TSX_CONTENT = """
import React from "react";
import { HashLoader } from "react-spinners";
import { useAppSelector } from "../hooks";

export const LoadingIndicator = () => {
  const isLoading = useAppSelector((state) => state.isLoading);

  if (!isLoading) return null;

  return (
    <div
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        width: "100%",
        height: "100%",
        backgroundColor: "rgba(0, 0, 0, 0.5)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        zIndex: 9999,
      }}
    >
      <HashLoader color={"#013d55"} size={120} />
    </div>
  );
};
"""

COMPONENTS_INDEX_TSX_CONTENT = """
import { LoadingIndicator } from "./LoadingIndicator";
import { FeedbackToast } from "./FeedbackToast";
export { LoadingIndicator, FeedbackToast };
"""
