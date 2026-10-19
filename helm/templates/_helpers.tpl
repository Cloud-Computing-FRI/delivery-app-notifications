{{/*
Template helpers for the notifications chart.

By default the Service name is the bare chart name ("notifications"), NOT a
release-prefixed name, so sibling services (and the UI) can address it at a
stable DNS name. Set fullnameOverride to change it.
*/}}

{{- define "notifications.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "notifications.fullname" -}}
{{- default (include "notifications.name" .) .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "notifications.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/* Common labels. Call with the root context ($). */}}
{{- define "notifications.labels" -}}
helm.sh/chart: {{ include "notifications.chart" . }}
app.kubernetes.io/part-of: delivery-app
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/* Selector labels. Call with the root context ($). */}}
{{- define "notifications.selectorLabels" -}}
app.kubernetes.io/name: {{ include "notifications.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/component: notifications
{{- end -}}

{{/* Host of the database: the in-cluster service unless database.host overrides it. */}}
{{- define "notifications.dbHost" -}}
{{- if .Values.database.host -}}
{{- .Values.database.host -}}
{{- else -}}
{{- printf "%s-db" (include "notifications.fullname" .) -}}
{{- end -}}
{{- end -}}

{{/* Name of the Secret holding DATABASE_URL (pre-created one in prod). */}}
{{- define "notifications.dbSecret" -}}
{{- default (printf "%s-db" (include "notifications.fullname" .)) .Values.database.existingSecret -}}
{{- end -}}
