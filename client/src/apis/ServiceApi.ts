/* tslint:disable */
/* eslint-disable */
/**
 * NLP Sandbox Deidentifier API
 * The OpenAPI specification implemented by NLP Sandbox PHI Deidentifiers. # Overview TBA 
 *
 * The version of the OpenAPI document: 0.2.2
 * Contact: thomas.schaffter@sagebionetworks.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import {
    Service,
    ServiceFromJSON,
    ServiceToJSON,
} from '../models';

/**
 * 
 */
export class ServiceApi extends runtime.BaseAPI {

    /**
     * Get information about the service
     * Get service information
     */
    async serviceRaw(): Promise<runtime.ApiResponse<Service>> {
        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/service`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => ServiceFromJSON(jsonValue));
    }

    /**
     * Get information about the service
     * Get service information
     */
    async service(): Promise<Service> {
        const response = await this.serviceRaw();
        return await response.value();
    }

}